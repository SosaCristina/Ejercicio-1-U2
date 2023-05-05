from ClaseEmail import Email
from ClaseManejadorEmail import ManejadorEmail

if __name__=='__main__':
    
    print ("Ingresar su nombre")
    nombre= str(input())
    print("Ingresar ID")
    id=input()
    print("Ingresar dominio")
    dominio= input()
    print("Ingresar tipo de dominio")
    tipodom= input()
    print("Ingrese contraseña")
    contraseña=input()
    unEmail=Email()
    unEmail.inicializar(id,dominio,tipodom,contraseña)
    print("Estimado"+ nombre +"te enviaremos tus mensajes a la direccion" + unEmail.getEmail()) #item1
    unEmail.modificarContraseña() #item2 FUNCIONA
    unEmail2=Email()
    print("Ingresar correo electronico") 
    correo=input()
    contra=input("Ingresar contraseña")
    unEmail2.crearCorreo(correo,contra)
    lista=ManejadorEmail()
    lista.abrir()
    lista.mostrar()
    print("Ingresar identificador para comprobar si esta repetido")
    ident=input()
    lista.buscar_repetido(ident)



