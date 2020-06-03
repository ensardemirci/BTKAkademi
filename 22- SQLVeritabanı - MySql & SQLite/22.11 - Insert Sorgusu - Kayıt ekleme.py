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

list = []
while True:
    name = input('Ürün adı: ')
    price = float(input('Ürün fiyatı: '))
    imageUrl = input('image url: ')
    description = input('Açıklama: ')

    list.append((name,price,imageUrl,description))


    result = input('devam etmek istiyormusnuz ? (e/h):')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)

        insertProducts(list)
        break
# mycursor.execute('SHOW DATABASES')

# mycursor.execute('CREATE DATABASE mydatabase')

# for x in mycursor:
#     print(x)
