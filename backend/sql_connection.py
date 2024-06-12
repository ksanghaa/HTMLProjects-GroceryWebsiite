import mysql.connector
from mysql.connector import errorcode
from config import DATABASE_CONFIG

def get_sql_connection():
    try:
        cnx = mysql.connector.connect(
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            host=DATABASE_CONFIG['host'],
            database=DATABASE_CONFIG['database']
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
