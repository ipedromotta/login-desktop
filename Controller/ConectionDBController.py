import mysql.connector

host="localhost"
user="root"
passwd=""
database="usuarios"

class ConectionDBController:

    @staticmethod
    def get_connection():
        try:
            cnxn = mysql.connector.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )
            return cnxn
        except Exception as ex:
            return ex
