import psycopg2

conexion = psycopg2.connect(
        user='postgres',
        password='admin',
        host='127.0.0.1',
        port='5432',
        database='test_db'
        )
#Busqueda
# try:
#         with conexion:
#                 with conexion.cursor() as cursor:
#                         sentencia = 'SELECT * FROM personas WHERE id_persona IN %s'
#                         entrada = input('Proporciona los id de las personas (Separados por comas): ')
#                         llaves_primarias = (tuple(entrada.split(',')), ) 
#                         cursor.execute(sentencia, llaves_primarias)
#                         registros = cursor.fetchall()
#                         for registro in registros:
#                                 print(registro)
# except Exception as e:
#         print(f'Ocurrio un error {e}')
# finally:
#         conexion.close()



try:
        with conexion:
                with conexion.cursor() as cursor:
                        sentencia = 'INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s);'
                        valores = (('carlos', 'duty', 'Clara@email.com'), ('Maria', 'Tatiana', 'mtata@email.com'))
                        cursor.executemany(sentencia,valores)
                        registros_insertados = cursor.rowcount
                        print(f"Se registraron {registros_insertados} personas")

except Exception as e:
        print(f'Ocurrio un error, {e}')
finally:
        conexion.close()


# try:
#         with conexion:
#                 with conexion.cursor() as cursor:
#                         sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s;'
#                         valores = (('carlos', 'Sanchez', 'CSanchez@email.com', 4),
#                                    ('Luis', 'Sanchez', 'LSanchez@email.com', 1))
#                         cursor.executemany(sentencia,valores)
#                         registros_actualizados = cursor.rowcount
#                         print(f"Se actualizaron {registros_actualizados} personas")

# except Exception as e:
#         print(f'Ocurrio un error, {e}')
# finally:
#         conexion.close()



# try:
#         with conexion:
#                 with conexion.cursor() as cursor:
#                         sentencia = 'DELETE FROM personas WHERE id_persona IN %s;'
#                         entradas = input("Digite las personas que quiera eliminar (Separados por comas): ")
#                         llaves_primarias = (tuple(entradas.split(',')), ) 

#                         valores = (5,)
#                         cursor.execute(sentencia,llaves_primarias)
#                         registros_eliminados = cursor.rowcount
#                         print(f"Se eliminaron {registros_eliminados} personas")

# except Exception as e:
#         print(f'Ocurrio un error, {e}')
# finally:
#         conexion.close()


  
  