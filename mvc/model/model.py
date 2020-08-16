import mysql.connector
from mysql.connector import errorcode

class Alumnos():
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_agenda', 
                password='Agenda_2020',
                host='127.0.0.1',
                port=3306,
                database='escuela')
            print("Conectado")
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print("Error connect: ", e)
    
    def select(self):
        try:
            self.connect()
            query=('SELECT * FROM alumnos;')
            self.cursor.execute(query)
            result=[]
            for row in self.cursor:
                r = {
                    'id_persona' : row[0],
                    'matricula' : row[1],
                    'nombre' : row[2],
                    'ap_paterno' : row[3],
                    'ap_materno' : row[4],
                    'edad' : row[5],
                    'fecha_nac' : row[6],
                    'genero' : row[7],
                    'estado' : row[8],
                    }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print("Error Select: ", e)
            result =[]
            return result
    
    def view(self, id_persona):
        try:
            self.connect()
            query=('SELECT * FROM alumnos where id_alumno = %s;')
            val_tupla=(id_persona,)
            self.cursor.execute(query, val_tupla)
            result=[]
            for row in self.cursor:
                r = {
                    'id_persona' : row[0],
                    'matricula' : row[1],
                    'nombre' : row[2],
                    'ap_paterno' : row[3],
                    'ap_materno' : row[4],
                    'edad' : row[5],
                    'fecha_nac' : row[6],
                    'genero' : row[7],
                    'estado' : row[8],
                    }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print("Error View: ", e)
            result=[]
            return result
    
    def insert(self, matricula, nombre, ap_paterno, ap_materno,edad, fecha_nac, genero, estado):
        try:
            self.connect()
            query=('INSERT INTO alumnos (matricula, nombre, ap_paterno, ap_materno, edad, fecha_nac, genero, estado) values(%s, %s, %s, %s, %s, %s, %s, %s)')
            val_tupla=(matricula, nombre, ap_paterno, ap_materno, edad, fecha_nac, genero, estado)
            self.cursor.execute(query, val_tupla)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print("Error Insert: ", e)
            return False

    def delete(self, id_persona):
        try:
            self.connect()
            query=('DELETE FROM alumnos WHERE id_alumno = %s')
            val_tupla=(id_persona, )
            self.cursor.execute(query, val_tupla)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print("Error Delete: ", e)
            return False

    def update(self, id_persona, matricula, nombre, paterno, materno, edad, fecha, genero, estado):
        try:
            self.connect()
            query = ("UPDATE alumnos SET matricula=%s, nombre=%s, ap_paterno=%s, ap_materno=%s, edad=%s, fecha_nac=%s, genero=%s, estado=%s WHERE id_alumno=%s;")
            val_tupla = (matricula, nombre, paterno, materno, edad, fecha, genero, estado, id_persona )
            self.cursor.execute(query, val_tupla)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print("Error Update: ", e)
            return False

objeto=Alumnos()
objeto.connect()
for row in objeto.select():
    print(row)