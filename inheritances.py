class Person():
    def __init__(self,fName,lName) :
        self.fName=fName
        self.lName=lName
        print("Person Createt")

    def whoAmI(self):
        print("I am a person")

class Student(Person):
    def __init__(self, fName, lName):
        Person.__init__(self,fName, lName)
        print("Student createt")

    def whoAmI(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self, fName, lName,branch):
        super().__init__(fName, lName)
        self.branch=branch

    def whoAmI(self):
        print(f"I am a {self.branch} teacher")

p1=Person("Yunus","Aydın")
s1=Student("Emirhan","Feten")
t1=Teacher("Onur","Özcan","Matematik")

print(s1.fName + ' ' + s1.lName)
print(p1.fName + ' ' + p1.lName)
print(t1.fName + ' ' + t1.lName)

p1.whoAmI()
s1.whoAmI()
t1.whoAmI()