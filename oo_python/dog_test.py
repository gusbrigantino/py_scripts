class Dog:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        print(self.age)

    def set_age(self, new_age):
        self.age = new_age

    def add_year(self):
        self.age += 1

    def bark(self):
        print("bark")

d = Dog("nelly", 4)
d.get_name()
d.get_age()
d.bark()
d.add_year()
d.get_age()
d.set_name("buster")
d.get_name()