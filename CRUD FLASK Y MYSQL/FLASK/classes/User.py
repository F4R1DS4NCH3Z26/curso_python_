from models.entities.User import User as UserEnt

class User():

    def __init__(self, mysql):
        self.mysql = mysql
    
    def login(self, user):
        try:
            cur = self.mysql.connection.cursor()
            sql = "SELECT * FROM user WHERE username = '{}';".format(user.username)
            cur.execute(sql)
            data = cur.fetchone()

            if data != None:
                user = UserEnt(data[0], data[1], UserEnt.check_password(data[3], user.password), data[2])
                return user

        except Exception as ex:
            raise Exception(ex)   

    def get_by_id(self, id):
        try:
            cur = self.mysql.connection.cursor()
            sql = "SELECT * FROM user WHERE id = '{}';".format(id)
            cur.execute(sql)
            data = cur.fetchone()

            if data != None:
                logger_user = UserEnt(data[0], data[1], None, data[2])
                return logger_user

        except Exception as ex:
            raise Exception(ex)   

