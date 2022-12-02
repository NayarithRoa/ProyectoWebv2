from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, nombre, telefono, clave="") -> None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.clave = clave

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    #print(generate_password_hash("12345"))
    #python .\src\models\entidades\Usuario.py
