def cube():
    for i in range(5):
        yield i**3  # bu değer bellekte yer tutmaz. O anlık gösterilir ve bellekten silinir. geriye dönük olarak bu veriye ulaşamayız.
                    # İşimiz eğer değerleri sadece göstermekse kullanılabilir.

for i in cube():
    print(i)