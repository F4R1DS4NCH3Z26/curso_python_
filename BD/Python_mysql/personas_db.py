import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="personas"
)

mi_cursor = personas_db.cursor()

sentancia_sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s,%s,%s) "
valores = ("Nathalie", "Pelaez", 24)
mi_cursor.execute(sentancia_sql, valores)
personas_db.commit()

mi_cursor.execute("SELECT * FROM personas")
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)
personas_db.close()