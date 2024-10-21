from logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f"""
            Id Usuario: {self._id_usuario}, 
            Nombre de Usuario: {self._username},
            Contraseña: {self._password}
        """
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    
    @password.setter
    def apellido(self, password):
        self._password = password
 

if __name__ == "__main__":
    usuario1 = Usuario(1,"FSanchez", "1234")
    log.debug(usuario1)
    # simular insert
    usuario1 = Usuario(username='juan', password='seanz')
    log.debug(usuario1)
    # simular delete
    usuario1 = Usuario(id_usuario=1)
    log.debug(usuario1)