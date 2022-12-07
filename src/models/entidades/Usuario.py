#Paquete para encriptar la clave
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class UserLogin(UserMixin):

    def __init__(self, id, nombre, correo, telefono, clave) -> None:
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.clave = clave
    #classmethod, para utilizar la clase sin instanciarla
    @classmethod
    #hashed_password es la clave encriptada
    #Permite verificar si la clave encriptada coincide con el valor real de la clave
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    @classmethod
    def generar_password(self,password):
        return generate_password_hash(password)

    #print(generate_password_hash("123456789"))
    #FORMA DE CORRER EL ARCHIVO PARA VER LA CLAVE GENERADA: python .\src\models\entidades\Usuario.py
class UserRegister(UserMixin):
   def __init__(self, id,sexo, edad, estrato, vivienda, escolaridad,
                ocupacion, afilicacionSalud, discapacidad, enfermedad, cuidador, estadoCivil="") -> None:
        self.id = id
        self.sexo = sexo
        self.edad = edad
        self.estrato = estrato
        self.vivienda = vivienda
        self.escolaridad = escolaridad
        self.ocupacion = ocupacion
        self.afilicacionSalud = afilicacionSalud
        self.discapacidad = discapacidad
        self.enfermedad = enfermedad
        self.cuidador = cuidador
        self.estadoCivil = estadoCivil
        

        
   
