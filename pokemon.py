class Pokemon:
    def __init__(self, nombre, color, tipo):
        self.nombre = nombre
        self.color = color
        self.tipo = tipo

    def saludar(self):
        print("Hola soy " + self.color + self.nombre + '\033[0m')

    def name(self):
        return(self.color + self.nombre + '\033[0m')
