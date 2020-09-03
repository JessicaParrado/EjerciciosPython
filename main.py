print("Binevenido, con este programa podrá concocer su edad en el 2070");

edad=(-1);
anio=-1;
while edad<=0:
    edad = int(input("Introduzca su edad: "));
    if edad<0:
        print("Debe introducir un número mayor a cero");
    else:
        print("Se ha registrado su edad");

while anio<=0:
    anio = int(input("Introduzca el año actual: "));
    if anio<0:
        print("Debe introducir un año mayor a cero");
    else:
        print("Se ha registrado el año");

