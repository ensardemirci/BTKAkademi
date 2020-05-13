def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return f'{role} rolü {page} sayfasına ulaşabilir '
        else:
            return f'{role} rolü {page} sayfasına ulaşamaz '
    return inner

user1 = yetki_sorgula('Product Edit')  # Burada yetki sorgula fonks. içinden inner fonks. user1 e atanıyor.
print(user1('Admin')) # user1 artık inner fonksiyonuna eşit ve ona gönderilen eski sayfa bilgisinide içinde taşıyor.
print(user1('User'))  # böylece çalıştırıldığında kullanıcı girişi inner fonks. üzerinden yapılıyor.