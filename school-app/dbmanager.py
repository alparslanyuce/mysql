import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from SchoolClass import SchoolClass

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            return SchoolClass.createClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentByClassId(self, classid):
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)
    
    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata:', err)
    
    def editStudent(self, student: Student):
        sql = "update student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s where id=%s" 
        value = (student.studentNumber, student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt düzenlendi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def deleteStudent(self, studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass
    
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()
        print('db bağlantısı kapatıldı')

db = DbManager()
# student= db.getStudentById(7)
# student[0].name="murat"
# student[0].studentNumber = "501"
# # db.addStudent(student[0])
# db.editStudent(student[0])

# students = db.getStudentByClassId(1)
# print(students[0])

# db.closeConnection()
