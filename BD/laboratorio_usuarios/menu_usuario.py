from usuario_dao import UsuarioDAO
from usuarios import Usuario
from logger_base import log

opcion = None
while opcion != 5:
    print("Opciones:")
    print("1. Listar usuarios")
    print("2. Agregar usuarios")
    print("3. Modificar")
    print("4. Eliminar usuarios")
    print("5. Salir")

    opcion = int(input("Escribe tu opcion (1-5): "))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = str(input("Insertar un nombre de usuario: ")) 
        password_var = str(input("Insertar una contraseña: "))
        valores_usuario = Usuario(username=username_var, password=password_var)
        usuarios = UsuarioDAO.insertar(valores_usuario)
        log.info(f"Usuarios insertados {usuarios}")
    elif opcion == 3:
        username_var = str(input("Insertar un nombre de usuario: ")) 
        password_var = str(input("Insertar una contraseña: "))
        id_usuario_var = str(input("Insertar id usuario: "))
        valores_usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios = UsuarioDAO.actualizar(valores_usuario)
        log.info(f"Usuarios actualizados {usuarios}")
    elif opcion == 4:
        id_usuario_var = str(input("Insertar id usuario: "))
        valores_usuario = Usuario(id_usuario=id_usuario_var)
        usuarios = UsuarioDAO.eliminar(valores_usuario)
        log.info(f"Usuarios eliminado {usuarios}")
else:
    log.info('Salimos de la aplicacion')