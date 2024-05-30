import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database='basededatos',
            user='root',
            password='03579'
        )

    def inserta_legajo(self, legajo, Apellido_y_nombre, direccion, localidad, cp, fecha_ingreso, Antigüedad, Fecha_Nacimiento, Edad, DNI, nro, cat, oficina, Nombre_Oficina, Secretaria, sindicato, Sepelio, Mutual, solo_4, Coseguro, Seguro, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO, Nro_De_Afiliado, Fecha_De_Afiliacion):
        cur = self.conexion.cursor()

        sql = '''INSERT INTO sindicato (LEGAJO, APELLIDO_Y_NOMBRE, DIRECCION, LOCALIDAD, CP, FECHA_INGRESO, ANTIGUEDAD, FECHA_DE_NACIMIENTO, EDAD, DNI, NRO, CAT, OFICINA, NOMBRE_OFICINA, SECRETARIA, SINDICATO, SEPELIO, MUTUAL, SOLO_4, COSEGURO, SEGURO, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO, Nro_De_Afiliado, Fecha_De_Afiliacion) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        
        values = (legajo, Apellido_y_nombre, direccion, localidad, cp, fecha_ingreso, Antigüedad, Fecha_Nacimiento, Edad, DNI, nro, cat, oficina, Nombre_Oficina, Secretaria, sindicato, Sepelio, Mutual, solo_4, Coseguro, Seguro, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO, Nro_De_Afiliado, Fecha_De_Afiliacion)
        
        cur.execute(sql, values)
        self.conexion.commit()
        cur.close()

    def mostrar_legajo(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM sindicato"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_legajo(self, nombre_legajo):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM sindicato WHERE LEGAJO = %s"
        cur.execute(sql, (nombre_legajo,))
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

 
