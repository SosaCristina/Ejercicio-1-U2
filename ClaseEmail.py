from re import split
import string


class Email:
    __idcuenta:string
    __dominio:string
    __tipodominio:string
    __contraseña:string

    def inicializar (self, id, dom, tipodom, clave):
        self.__idcuenta=id
        self.__dominio=dom
        self.__tipodominio=tipodom
        self.__contraseña=clave

    def getId(self):
        return self.__idcuenta    

    def getEmail (self):
        return self.__idcuenta + "@" + self.__dominio + "." + self.__tipodominio    

    def modificarContraseña(self):
        print("Para modoficar la contraseña, ingrese contraseña actual")
        actual=input()
        if (actual == self.__contraseña):
            print("Ingresar contraseña nueva")
            nueva=input()
            self.__contraseña=nueva
        else:
            print ("Contraseña incorrecta, no es posible modificarla")   

    def crearCorreo(self, correo,contraseña):
        arre1= correo.split ("@")
       
        self.__idcuenta=arre1[0]
        
        arre2= arre1[1].split (".")
        self.__dominio=arre2[0]
        self.__tipodominio=arre2[1]
        self.__contraseña=contraseña
        print("Correo creado exitosamente")
        

    def __str__ (self):
        return "%s @ %s . %s - contraseña:%s " %(self.__idcuenta,self.__dominio,self.__tipodominio,self.__contraseña)







