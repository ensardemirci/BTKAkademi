import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='123qwe123',
    database = 'node-app'
    )
    cursor = connection.cursor()

    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)'
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id numarası: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('Hata: ',err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı')

def insertProducts(list):
    connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='123qwe123',
    database = 'node-app'
    )
    cursor = connection.cursor()

    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)'
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id numarası: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('Hata: ',err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı')

def getProducts():
    connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='123qwe123',
    database = 'node-app'
    )
    cursor = connection.cursor()

    # cursor.execute('Select * From Products')
    cursor.execute('Select name,price From Products')

    # result = cursor.fetchall()
    result = cursor.fetchone()
    print(f'Name: {result[0]} Price: {result[1]}')
    # for product in result:
    #     # print(f'Name: {product[1]} Price: {product[2]}')
    #     print(f'Name: {product[0]} Price: {product[1]}')

getProducts()