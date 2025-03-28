class Profesor:

    def __init__(self, mysql):
        self.mysql = mysql
    
    def get_profesor(self, id = None):
        cur = self.mysql.connection.cursor()
        sql = "SELECT * FROM profesor"

        if id:
            sql += f" WHERE id = {id};"

        cur.execute(sql)
        data = cur.fetchall()
        
        return data
    
    def create_profesor(self, data):
        
        document = data.get('document') 
        name = data.get('name') 
        lastname = data.get('lastname') 
        second_lastname = data.get('second_lastname') 
        city = data.get('city') 
        address = data.get('address') 
        phone = data.get('phone') 
        origin_date = data.get('origin_date') 
        sex = data.get('sex') 
        state_id = data.get('state_id')
        cur = self.mysql.connection.cursor()

        result = cur.execute(
            f"""
                INSERT INTO profesor 
                (nif, 
                nombre, 
                apellido1, 
                apellido2, 
                ciudad, 
                direccion, 
                telefono, 
                fecha_nacimiento, 
                sexo, 
                id_departamento)
                    
                VALUES (
                {document},
                '{name}', 
                '{lastname}', 
                '{second_lastname}', 
                '{city}', 
                '{address}', 
                '{phone}', 
                '{origin_date}', 
                '{sex}', 
                '{state_id}' 
                ) 
                """
                )
       
        self.mysql.connection.commit()
        return result

    def edit_profesor(self, data):
        
        id = data.get('id') 
        document = data.get('document') 
        name = data.get('name') 
        lastname = data.get('lastname') 
        second_lastname = data.get('second_lastname') 
        city = data.get('city') 
        address = data.get('address') 
        phone = data.get('phone') 
        origin_date = data.get('origin_date') 
        sex = data.get('sex') 
        state_id = data.get('state_id')
        cur = self.mysql.connection.cursor()

        print(f"""UPDATE profesor SET 
                nif = '{document}',
                nombre = '{name}', 
                apellido1 = '{lastname}', 
                apellido2 = '{second_lastname}', 
                ciudad = '{city}', 
                direccion = '{address}', 
                telefono = '{phone}', 
                fecha_nacimiento = '{origin_date}', 
                sexo = '{sex}', 
                id_departamento = '{state_id}' 
                WHERE id = {id}; 
                """)

        result = cur.execute(
            f"""UPDATE profesor SET 
                nif = '{document}',
                nombre = '{name}', 
                apellido1 = '{lastname}', 
                apellido2 = '{second_lastname}', 
                ciudad = '{city}', 
                direccion = '{address}', 
                telefono = '{phone}', 
                fecha_nacimiento = '{origin_date}', 
                sexo = '{sex}', 
                id_departamento = '{state_id}' 
                WHERE id = {id};  
                """
                )
       
        self.mysql.connection.commit()
        return result
    
    def delete_profesor(self, id):
        cur = self.mysql.connection.cursor()
        data = cur.execute("DELETE FROM profesor WHERE id = %s", id)
        return data
    
