from ClaseEmail import Email
import csv
import os


class Menu :
    __op= int
    def __init__ (self):
        self.__op=None
    def getOpcion (self):
        return self.__op
    def manejoMenu (self,op,xCorreo):
        if op == 1:
            self.opcion1(xCorreo)
        elif op == 2:
            self.opcion2(xCorreo)
        elif op == 3:
            self.opcion3()
        else:
            self.Salir()

    def opcion1 (self,xCorreo):
        print("Ingresaremos su direccion de e-mail")
        nom=input('Ingresar su nombre: ')
        correo=input('Ingresar su nuevo correo: ')
        contrasenia=input('Ingrese su contrasenia: ')
        xCorreo.crearCuenta(correo,contrasenia)
        print("Estimado {} te enviaremos tus mensajes a la dirección {}".format(nom,xCorreo.retornaMail()))
        
    def opcion2 (self,xCorreo):
        print()
        print('--------- MODIFIQUE CONTRASENIA')
        xCorreo.modificaCont()
        os.system('pause')
        os.system('cls')
        
    def opcion3 (self):
        cont = 0
        path_archivo='Actividad1\Prueba.csv'
        archivo = open(path_archivo,"r")
        reader = csv.reader(archivo,delimiter=',')
        id=input('Ingrese identificador a buscar: ')
        for fila in reader:
            if fila[0] == id:
                cont += 1
        print("La cantidad de personas con el identificador '{}' es: {}".format(id,cont))
        if cont > 1:
            print("El identificador se repite")
        else:
            print("El identificador no se repite")
        archivo.close()
        os.system('pause')
        os.system('cls')
        
    def Salir(self):
        print('Salir')
        os.system('Pause')
