def conocerCaracter(palabra):
    primeraLetra = palabra[0]
    longitud = len(palabra)
    ultimaLetra = palabra[longitud-1]
    print("La primera letra es ", primeraLetra, " y la última letra es ",ultimaLetra)
    return primeraLetra+ultimaLetra;
def main():
    print("Binevenido, con este programa podrá concocer el primer y último carácter")

    palabra = input("Introduzca la palabra: ")
    conocerCaracter(palabra)

if __name__ == '__main__':
    main()
