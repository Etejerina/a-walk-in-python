(function () {
  var storageKey = "a-walk-in-python-theme";
  var root = document.documentElement;
  var mediaQuery = window.matchMedia
    ? window.matchMedia("(prefers-color-scheme: dark)")
    : null;

  function getStoredTheme() {
    try {
      return localStorage.getItem(storageKey);
    } catch (error) {
      return null;
    }
  }

  function storeTheme(theme) {
    try {
      localStorage.setItem(storageKey, theme);
    } catch (error) {
      // Theme changes still work for the current page when storage is unavailable.
    }
  }

  function normalizeTheme(theme) {
    return theme === "dark" || theme === "light" ? theme : null;
  }

  function systemTheme() {
    return mediaQuery && mediaQuery.matches ? "dark" : "light";
  }

  function updateToggle(theme) {
    var toggles = document.querySelectorAll("[data-theme-toggle]");

    toggles.forEach(function (toggle) {
      toggle.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    });
  }

  function setTheme(theme, persist) {
    root.setAttribute("data-theme", theme);
    root.style.colorScheme = theme;
    if (persist) {
      storeTheme(theme);
    }
    updateToggle(theme);
  }

  function currentTheme() {
    return normalizeTheme(root.getAttribute("data-theme")) || systemTheme();
  }

  setTheme(normalizeTheme(getStoredTheme()) || systemTheme(), false);

  document.addEventListener("DOMContentLoaded", function () {
    updateToggle(currentTheme());

    document.addEventListener("click", function (event) {
      var target = event.target;
      if (!target || !target.closest) {
        return;
      }

      var toggle = target.closest("[data-theme-toggle]");
      if (!toggle) {
        return;
      }

      setTheme(currentTheme() === "dark" ? "light" : "dark", true);
    });
  });

  if (mediaQuery) {
    var handleSystemThemeChange = function () {
      if (!normalizeTheme(getStoredTheme())) {
        setTheme(systemTheme(), false);
      }
    };

    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener("change", handleSystemThemeChange);
    } else if (mediaQuery.addListener) {
      mediaQuery.addListener(handleSystemThemeChange);
    }
  }
})();
