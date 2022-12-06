class miClase:
    x = 5


p1 = miClase()
print(p1.x)


class persona:
    nombre = str
    edad = int

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Su nombre es {self.nombre}, y su edad es {self.edad}."


p2 = persona("Diego", 25)

print(p2)


class Persona2:
    nombre = str
    edad = int
    cedula = int

    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cédula = cedula

    def __str__(self):
        return f"Hola mi nombre es  {self.nombre}. Mi edad es: {self.edad} y mi numero de cedula es: {self.cedula}"


p3 = Persona2("Andrea", 22, 1753650686)
p3.nombre = "Dylan"
p3.cedula = "1753650686"

print(p3)


class persona3:
    nombre = str
    edad = int
    altura = int

    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura

    def __str__(self):
        return f"Su nombre es {self.nombre}. tu edad es: {self.edad} y su estatura {self.estatura}"


p4 = persona3("Juan", 18, 170)

print(p4)
