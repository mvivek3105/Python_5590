class Person:
    def _init_(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
class Student(Person):
    StudentCount = 0
    def _init_(self,name,email,student_id):
        Person._init_(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        Person.display(self)
        print("Student Id: ",self.student_id)
class Librarian(Person):
    StudentCount = 0
    def _init_(self,name,email,employee_id):
        super()._init_(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Details:")
        Person.display(self)
        print("Employee Id: ",self.employee_id)
class Book():
    def _init_(self, bname, author, book_id):
        self.book_name = bname
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)
class Borrow_Book(Student,Book):
    def _init_(self, name, email, student_id, bname, author, book_id):
        Student._init_(self,name,email,student_id)
        Book._init_(self, bname, author, book_id)
    def display(self):
        print("Borrowed Book Details:")
        Student.display(self)
        Book.display(self)
list1= []
list1.append(Student('World', 'world@gmail.com', 456))
list1.append(Student('Hello', 'Hello@gmail.com', 123))
list1.append(Librarian('Emp1', 'emp@gmail.com', 789))
list1.append(Librarian('Emp2', 'emp1@gmail.com', 847))
list1.append(Book('JAVA', 'Herbert Schlidit', 9023301))
list1.append(Book('LINUX PROGRAMMING', 'OReily', 847902))
list1.append(Borrow_Book('World', 'world@gmail.com', 456, 'JAVA', 'Herbert Schlidit', 9023301))
for obj, item in enumerate(list1):
    item.display()
    print("\n")
    if obj == len(list1)-1:
        item.displayCount()