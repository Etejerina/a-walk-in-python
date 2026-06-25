from __future__ import annotations

import contextlib
import io
import json
import multiprocessing
import queue
import sys
import traceback
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def printable(text: object) -> str:
    return str(text).encode("ascii", "backslashreplace").decode("ascii")


def source_from_cell(cell: dict[str, object]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(str(line) for line in source)
    return str(source)


def run_notebook(path: Path, stop_on_error: bool) -> dict[str, object]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace: dict[str, object] = {"__name__": "__main__"}
    failures: list[dict[str, str | int]] = []
    code_cells = 0

    for index, cell in enumerate(notebook.get("cells", []), start=1):
        if cell.get("cell_type") != "code":
            continue
        code_cells += 1
        code = source_from_cell(cell)
        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout):
                exec(compile(code, str(path), "exec"), namespace)
        except Exception:
            error = traceback.format_exception_only(sys.exception())
            failures.append(
                {
                    "cell": index,
                    "error": "".join(error).strip(),
                    "preview": code.strip().splitlines()[0] if code.strip() else "",
                }
            )
            if stop_on_error:
                break

    return {"code_cells": code_cells, "failures": failures, "timed_out": False}


def worker(path: str, stop_on_error: bool, result_queue: multiprocessing.Queue) -> None:
    try:
        result_queue.put(run_notebook(Path(path), stop_on_error))
    except Exception:
        result_queue.put(
            {
                "code_cells": 0,
                "failures": [
                    {
                        "cell": 0,
                        "error": traceback.format_exc(),
                        "preview": "runner failure",
                    }
                ],
                "timed_out": False,
            }
        )


def run_with_timeout(path: Path, stop_on_error: bool, timeout: int) -> dict[str, object]:
    result_queue: multiprocessing.Queue = multiprocessing.Queue()
    process = multiprocessing.Process(
        target=worker,
        args=(str(path), stop_on_error, result_queue),
    )
    process.start()
    process.join(timeout)
    if process.is_alive():
        process.terminate()
        process.join()
        return {"code_cells": 0, "failures": [], "timed_out": True}
    try:
        return result_queue.get_nowait()
    except queue.Empty:
        return {
            "code_cells": 0,
            "failures": [{"cell": 0, "error": "No result returned", "preview": ""}],
            "timed_out": False,
        }


def main() -> int:
    timeout = 15
    stop_on_error = False

    total_cells = 0
    total_failures = 0
    for path in sorted(ROOT.rglob("*.ipynb")):
        result = run_with_timeout(path, stop_on_error, timeout)
        code_cells = int(result["code_cells"])
        failures = list(result["failures"])
        timed_out = bool(result["timed_out"])
        total_cells += code_cells
        total_failures += len(failures) + int(timed_out)

        status = "TIMED OUT" if timed_out else "OK" if not failures else "FAILED"
        print(f"{path.relative_to(ROOT)}: {status} ({code_cells} code cells)")
        for failure in failures:
            print(
                printable(
                    f"  cell {failure['cell']}: {failure['error']} "
                    f"[{failure['preview']}]"
                )
            )

    print(
        f"\nExecuted {total_cells} code cells across notebooks; "
        f"{total_failures} failed."
    )
    return 1 if total_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
