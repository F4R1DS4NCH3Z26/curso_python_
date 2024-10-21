from conexion import Conexion
from usuarios import Usuario
from logger_base import log
from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    """
    DAO (Data Access Object)
    CRUD (CREATE-READ-UPDATE-DELETE)
    """

    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = "INSERT INTO usuarios (username, password) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE usuarios SET username=%s, password=%s WHERE id_usuario = %s"
    _ELIMINAR = "DELETE FROM usuarios WHERE id_usuario = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Usuario insertado: {usuario}")              
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Usuario actualizado: {usuario}")              
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Usuario eliminado: {usuario}")              
            return cursor.rowcount
                    
if __name__ == "__main__":
    
    # Insertar datos
    # valores = Usuario(username="NPelaez", password="123456")
    # usuarios_insertados = UsuarioDAO.insertar(valores)
    # log.debug(f"Se insertaron {usuarios_insertados} personas") 

    #Actializar datos
    valores = Usuario(username = "asanchez", password="159753", id_usuario=2)
    usuarios_actualizados = Usuario.actualizar(valores)
    log.debug(f"Se actualizaron {usuarios_actualizados} usuario(s)") 

    # Eliminar datos
    # valores = Usuario(id_persona='1',)
    # personas_actualizadas = UsuarioDAO.eliminar(valores)
    # log.debug(f"Se elimiraron {personas_actualizadas} personas") 

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)