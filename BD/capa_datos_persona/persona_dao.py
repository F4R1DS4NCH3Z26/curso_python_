from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool

class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (CREATE-READ-UPDATE-DELETE)
    """

    _SELECCIONAR = 'SELECT * FROM personas ORDER BY id_persona'
    _INSERTAR = "INSERT INTO personas (nombre, apellido, email) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"
    _ELIMINAR = "DELETE FROM personas WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas
        
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {persona}")              
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona que actualizada: {persona}")              
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona que Eliminada: {persona}")              
            return cursor.rowcount
                    
if __name__ == "__main__":
    
    # Insertar datos
    # valores = Persona(nombre="Alejandra", apellido="Sanchez", email="ASanchez@email.com")
    # personas_insertadas = PersonaDAO.insertar(valores)
    # log.debug(f"Se insertaron {personas_insertadas} personas") 

    #Actializar datos
    # valores = Persona(6, nombre="Farid", apellido="Sanchez", email="FSanchez@email.com")
    # personas_actualizadas = PersonaDAO.actualizar(valores)
    # log.debug(f"Se actualizaron {personas_actualizadas} personas") 

    # Eliminar datos
    valores = Persona(id_persona='7',)
    personas_actualizadas = PersonaDAO.eliminar(valores)
    log.debug(f"Se elimiraron {personas_actualizadas} personas") 

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)