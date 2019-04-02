class SchoolMember:
    '''any one in school'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialized schoolmember:{})'.format(self.name))

    def tell(self):
        '''tell the detail'''
        print('Name:"{}",Age:"{}"'.format(self.name, self.age), end=" ") #end=" "下一次print可以不换行

class Teacher(SchoolMember):
    """represent a teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('salary:"{:d}"'.format(self.salary))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(initialized student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks:"{}"'.format(self.marks))

t = Teacher('Mr asd', 40, 30000)
s = Student('swaroop', 25, 75)

#print a blank line
print()

members = [t, s]
for member in members:
    member.tell()
