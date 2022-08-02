class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade

    def set_name(self, new_name):
        self.name = new_name
    
    def set_age(self, new_age):
        self.age = new_age
        
    def set_grade(self, new_grade):
        self.grade = new_grade


class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def get_name(self):
        return self.name

    def get_max_students(self):
        return self.max_students

    def get_students(self):
        return self.students

    def set_name(self, new_name):
        self.name = new_name
    
    def set_max_students(self, new_max_students):
        self.name = new_max_students

    def set_students(self, new_students):
        self.students = new_students

    def add_student(self, new_student):
        if len(self.students) < self.max_students:
            self.students.append(new_student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for x in self.students:
            total += x.get_grade()
        
        return total / len(self.students)


s1 = Student("gus", 23, 80)
s2 = Student("luke", 20, 75)
s3 = Student("tony", 22, 99)

course1 = Course("agbiz", 2)
course1.add_student(s3)
course1.add_student(s1)

print(course1.get_average_grade())
