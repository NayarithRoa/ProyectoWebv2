from .entidades.Usuario import UserLogin,UserRegister
import mysql.connector

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            conn=db.connect()#Conectarse a la base de datos
            cursor=conn.cursor()#Almacenar la instruccion SQL
            sql = """SELECT id, nombre, telefono, clave FROM persona 
                    WHERE telefono = '{}'""".format(user.telefono)
            cursor.execute(sql) #Ejecutar la instruccion almacenada
            row = cursor.fetchone() #devolver toda la informacion la consulta 
            if row != None:
                user = UserLogin(row[0], row[1], row[2], UserLogin.check_password(row[3], user.clave) )
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
                user = UserLogin(row[0], row[1], row[2],None)
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def registrardatosbasicos(self, db, user):
        try:
            conn=db.connect()#Conectarse a la base de datos
            cursor=conn.cursor()#Almacenar la instruccion SQL
            sql = """UPDATE persona SET sexo=%s, edad=%s, estrato=%s, vivienda=%s, escolaridad=%s,
                    ocupacion=%s, afilicacionSalud=%s, discapacidad=%s, enfermedad=%s, cuidador=%s, estadoCivil=%s
                    WHERE id= %s;""" 
            datos=(user.sexo,user.edad,user.estrato,user.vivienda,user.escolaridad,user.ocupacion,user.afilicacionSalud,user.discapacidad, user.enfermedad,user.cuidador,user.estadoCivil, user.id) 
            cursor.execute(sql, datos) #Ejecutar la instruccion almacenada
            row = cursor.rowcount#devolver toda la informacion la consulta 
            if row != None:
                conn.commit() #Cerrar la conexion que se realizó antes
                return row
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def registrarusuario(self, db, user):
        try:
            conn=db.connect()#Conectarse a la base de datos
            cursor=conn.cursor()#Almacenar la instruccion SQL
            sql = """INSERT INTO persona (id, nombre, correo, telefono, clave, sexo, edad, estrato, vivienda, escolaridad,
                    ocupacion, afilicacionSalud, discapacidad, enfermedad, cuidador, estadoCivil)
                    VALUES (NULL, %s,%s, %s,%s,'', '', '', '', '', '', '', '', '', '', '');""" 
            datos=(user.nombre, user.correo, user.telefono, user.clave) 
            cursor.execute(sql, datos) #Ejecutar la instruccion almacenada
            row = cursor.rowcount#devolver toda la informacion la consulta 
            if row != None:
                conn.commit() #Cerrar la conexion que se realizó antes
                return row
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    