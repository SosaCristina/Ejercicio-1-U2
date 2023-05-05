from ClaseEmail import Email
import csv

class ManejadorEmail:
    __listaEmail=[]

    def __init__(self):
        self.__listaEmail=[]

    def agregar (self,unEmail):
        self.__listaEmail.append(unEmail)

    def abrir(self):
        archivo=open('C:\\Users\\chili\\POO archivos\\listadirecciones.csv')
        reader=csv.reader(archivo,delimiter=",")
        bandera=True
        for fila in reader:
                if bandera:
                    "saltear cabecera"
                    bandera= not bandera
            
                else:
                    correo=fila[0]
                    contraseña=fila[1]
                    unEmail=Email()
                    unEmail.crearCorreo(correo,contraseña)
                    self.agregar(unEmail)
        archivo.close()        
    
    def __str__(self):
        s=""
        for lista in self.__listaEmail:
            s += str(lista) +'\n'
        return s
    
    def mostrar (self):
        for email in self.__listaEmail:
            print(email)

    def buscar_repetido (self, ident):
        for email in self.__listaEmail:
            if (ident==email.getId()):
                print(email.getId())
                print("Este identificador esta repetido")
             
            else:
                print("El identificador no esta repetido")   
        
             

