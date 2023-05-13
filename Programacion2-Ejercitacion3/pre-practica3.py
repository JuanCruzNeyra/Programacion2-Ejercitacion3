"""Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.
Comisión : X
Grupo : X
Integrantes:
-Legajo XXXX,....
-Legajo YYYY,....
.
.""" 

class vehiculo():
    def __init__(self, marca: str, ruedas: int, color: str):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = False
        
    def arrancar(self):
        self.enMarcha = True
        if self.enMarcha == True:
            return "En marcha"
        else:
            return "Apagado"
        
        
    
    def TipoVehiculo(self):
        if self.ruedas == 4:
            return "Automovil"
        elif self.ruedas == 2:
            return "Motocicleta"
    
    def Mostrar(self):
        print("Marca: ", self.marca)
        print("Color: ", self.color)
        print("Tipo de vehiculo:", vehiculo1.TipoVehiculo())
        print("Estado: ", vehiculo1.arrancar())
        
vehiculo1 = vehiculo("Toyota", 4, "Rojo")
vehiculo1.arrancar()
vehiculo1.Mostrar()

        
        
