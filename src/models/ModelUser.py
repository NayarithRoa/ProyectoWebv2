from .entidades.Usuario import User
import mysql.connector

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            conn=db.connect()
            cursor=conn.cursor()
            sql = """SELECT id, nombre, telefono, clave FROM usuario 
                    WHERE telefono = '{}'""".format(user.telefono)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], User.check_password(row[3], user.clave) )
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, nombre, telefono FROM usuario WHERE id = {}".format(id)         
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2],None)
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    