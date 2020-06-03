from dbmanager import DbManager
import datetime
from Student import Student

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = '****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\nÇıkış(E/Ç)'
        while True:
            print(msg)
            islem = input('Seçim: ')
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                pass
            elif islem == 'E' or islem == 'Ç':
                break
            else:
                print('Yanlış Seçim yaptınız')
    def editStudent(self):


    def displayClasses(self):

        classes = self.db.getClasses()
        for c in classes:
            print(c.id, c.name)


    def displayStudents(self):
        self.displayClasses()

        classid = int(input('Hangi Sınıf:'))

        students = self.db.getStudentsByClassId(classid)
        print('Öğrenci Listesi')
        for index,std in enumerate(students):
            print((index+1),std.name,std.surname)


    def addStudent(self):
        self.displayClasses()
        classid = int(input('Hangi Sınıf:'))
        number = input('Numara: ')
        name = input('isim: ')
        surname = input('soyisim: ')
        year = int(input('yıl: '))
        month = int(input('ay: '))
        day = int(input('gün: '))
        birthdate = datetime.date(year,month,day)
        gender = input('E/K: ')

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)




app = App()
app.initApp()