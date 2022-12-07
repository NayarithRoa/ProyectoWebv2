from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin


class UserLogin(UserMixin):

    def __init__(self, id, nombre, correo, telefono, clave="") -> None:
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.clave = clave

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

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
        
    #print(generate_password_hash("12345"))
    #python .\src\models\entidades\Usuario.py
