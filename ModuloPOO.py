class Password:
    def __init__(self,contraseña,long=8):
        self.__Longitud = long
        self.__Contraseña = contraseña
    
    def getContraseña(self):
        return self.__Contraseña
    
    def getLongitud(self):
        return self.__Longitud

    def setLongitud(self,long):
        self.__Longitud = long
        
    def generarPassword(long):
        passW = input("Ingrese una contraseña de {} caracteres de longitud: ".format(long))
        while len(passW) != long:
            passW = input("La contraseña no cumple con lo solicitado\nIngrese una contraseña de 8 caracteres: ")
        return passW
    
    def MuestraContraseña(self):
        print(self.__Contraseña)

    def esFuerte(self,contraseña):
        May = False
        Min = False
        Num = False 
        Mayus = 0
        Minus = 0
        Nums = 0
        for i in range (len(contraseña)):
            if contraseña[i].isupper():
                Mayus += 1
            if contraseña[i].islower():
                Minus += 1
            if contraseña[i].isnumeric():
                Nums += 1
        if Mayus > 2:
            May = True
        if Minus > 1:
            Min = True 
        if Nums > 3:
            Num = True 
        
        if May and Min and Num:
            return True
        else:
            return False  

Largo = int(input("Ingrese el largo de la contraseña: ")) 
Contraseña = Password.generarPassword(Largo)         
Obj1 = Password(Contraseña,Largo)
Obj1.MuestraContraseña()
n = Obj1.esFuerte(Contraseña)

if n is True:
    print("La contraseña es fuerte.")
else:
    print("La contraseña es debil.")