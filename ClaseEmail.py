import menu

class Email:
    __idCuenta= str
    __dominio= str
    __tipoDominio= str
    __contrasenia= str
    def __init__ (self,cuenta=None,dominio=None,tDominio=None,cont=None):
        self.__idCuenta= cuenta
        self.__dominio= dominio
        self.__tipoDominio= tDominio
        self.__contrasenia= cont
    def retornaMail(self):
        return (self.__idCuenta +'@'+ self.__dominio +'.'+ self.__tipoDominio)
    def getDominio(self):
        return (self.__dominio)
    def crearCuenta(self,correo,cont):
        if (correo.find('@')!= -1):
            xCorreo= correo.split('@')
            user= xCorreo[0]
            if (xCorreo[1].find('.')!= -1):
                domCompleto= xCorreo[1].split('.')
                auxDominio= domCompleto[0]
                auxTipoDominio= domCompleto[1]
                self.__init__(user,auxDominio,auxTipoDominio,cont)
                print('Correo originado con exito')
            else: print('Error: El dominio no contiene punto')
        else: print ('Error: El correo ingresado no contiene @')
    def modificaCont (self):
        aux= input('Ingrese su contrasenia: ')
        while self.__contrasenia != aux:
            aux= input('Contrasenia incorrecta, intente nuevamente: ')
        self.__contrasenia= input('Ingrese su nueva contrasenia: ')
    
        

