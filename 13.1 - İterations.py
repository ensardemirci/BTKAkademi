liste = [1,2,3,4,5]

myiter = iter(liste)

while True:   # For döngüsünün yaptığı işi iyi anlamak için arka planda dönen işlşemleri görmemiz lazım.
    try:        # Bu ilerde iteretion yapılabilen bir class oluşturduğumuzda işimize yarayacaktır.
        print(next(myiter))
    except StopIteration:
        break

