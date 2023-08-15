# x = 'www.hola.com', 25
# x = "www.hola.com", 21, "ftp"

x = set((1, 2, 2))


match x:
    case host, port:
        print("http mode")
    case host, port, mode:
        print(f"{ mode } mode")
    case _:
        print(x)
