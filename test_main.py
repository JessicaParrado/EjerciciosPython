from unittest import TestCase

from main import conocerEdad
class Test(TestCase):

#        while edad <= 0 or edad > 2070:
 #           edad = int(input("Introduzca su edad: "));
  #          if edad < 0:
   #             print("Debe introducir un número mayor a cero");
    #        else:
     #           print("Se ha registrado su edad");

#    while anio <= 0:
 #       anio = int(input("Introduzca el año actual: "));
  #      if anio < 0:
   #         print("Debe introducir un año mayor a cero");
    #    else:
     #       print("Se ha registrado el año");


 def test_conocer_edad(self):
   self.assertEqual(69,conocerEdad(19,2020))
