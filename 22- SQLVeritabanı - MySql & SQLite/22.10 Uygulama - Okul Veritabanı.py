import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='123qwe123',
    database = 'schooldb'
    )

print(mydb)

# mycursor.execute('SHOW DATABASES')

# mycursor.execute('CREATE DATABASE mydatabase')

# for x in mycursor:
#     print(x)
