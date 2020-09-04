def saberPar(numero):
    respuesta=False;
    if numero % 2 == 0:
        print("True")
        print('El número ', numero, ' es par (True)')
        respuesta=True;
    else:
        print('El número ', numero, ' NO es par (False)')
    return respuesta;
def main():
    print("Binevenido, con este programa podrá concocer si un número es par o no");

    numero = int(input("Introduzca el número: "));
    saberPar(numero)

if __name__ == '__main__':
    main()