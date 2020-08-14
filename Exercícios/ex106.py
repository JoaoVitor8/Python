from time import sleep


def ajuda_interativa(n=""):
    while n.lower().strip() != "fim":
        linhas("SISTEMA DE AJUDA PyHelp", 42, 31)
        n = str(input("\033[0:30:mFunção ou Biblioteca > "))
        if n.lower().strip() != "fim":
            linhas(f"Acessando o manual de comando '{n}'", 44, 45)
            print(f"\033[0:1:40m")
            help(n)
        else:
            linhas("ATÉ LOGO", 41, 16)


def linhas(f, val, sp):
    print(f"\033[0:30:{val}m~" * sp)
    print(f"\t{f}")
    print("~"*sp)
    sleep(2)


ajuda_interativa()
