class Person:
    number_of_people = 0        #access via class or object

    def __init__(self, name) -> None:
        self.name = name
        Person.add_person()

    @classmethod
    def get_num_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def get_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name

p1 = Person("gus")

print(Person.get_num_of_people())