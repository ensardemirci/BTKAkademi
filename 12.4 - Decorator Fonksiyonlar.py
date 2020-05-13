def my_decarator(func):
    def wrapper():
        print('function öncesi işlemler')
        func()
        print('function sonrası işlemler')
    return wrapper
@my_decarator   # Burada decorator fonks. kullanımı gösterilmiştir. Görüldüğü gibi my_deco. fonk. içindeki func() fonksiyonunun yerini sayHello fonksiyonu almıştır.
def sayHello():
    print('hello')


sayHello()