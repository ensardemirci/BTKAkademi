import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='123qwe123',
    database = 'mydatabase'
    )

mycursor = mydb.cursor() #Workbench üzerinden çok daha rahat bir şekilde tablolar oluşturulabilir.
mycursor.execute('CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255) )')

# mycursor.execute('SHOW DATABASES')

# mycursor.execute('CREATE DATABASE mydatabase')

# for x in mycursor:
#     print(x)
