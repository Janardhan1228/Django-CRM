import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Pingpong123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Johnny")

print('All settu')