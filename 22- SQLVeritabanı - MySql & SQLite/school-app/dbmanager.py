import mysql.connector
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = 'Select * From Student Where id = %s'
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Hata: ',err)

    def getClasses(self):

        sql = 'Select * From Class '
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Hata: ', err)


    def getStudentsByClassId(self,classid):
        sql = 'Select * From Student Where classid = %s'
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Hata: ', err)

    def addStudent(self, student: Student):

        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')

        except mysql.connector.Error as err:
            print('hata:', err)

    def editStudent(self, student: Student):

        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s, classid=%s where id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')

        except mysql.connector.Error as err:
            print('hata:', err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print('db silindi.')


db = DbManager()

student = db.getStudentById(1)
student[0].name = 'Ahmet'


# db.addStudent(student[0])
db.editStudent(student[0])

# students = db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[6].name)