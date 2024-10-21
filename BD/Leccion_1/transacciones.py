import psycopg2 as bd

conexion = bd.connect(
        user='postgres',
        password='admin',
        host='127.0.0.1',
        port='5433',
        database='test'
        )


try:
    with conexion:
        with conexion.cursor() as cursor:
#     conexion.autocommit = False
                sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s);'
                valores = ('Alex', 'Rojas', 'ARojas@email.com')
                cursor.execute(sentencia,valores)


                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s;'
                valores = ('Luis', 'Sanchez', 'LSanchez@email.com', 1)
                cursor.execute(sentencia,valores)

                conexion.commit()
                print("Proceso terminado")

except Exception as e:
        conexion.rollback()
        print(f'Ocurrio un error,se hizo rollback: {e}')
finally:
        conexion.close()
