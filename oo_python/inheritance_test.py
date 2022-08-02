class Pet:
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
    
    def show(self):
        print(self.name)
        print(self.age)

    def speak(self):
        print("hello")


class Cat(Pet):

    def speak(self):
        print("Meow")

class Dog(Pet):
    
    def speak(self):
        print("Bark")

class Fish(Pet):
    def __init__(self, name, age, color) -> None:       #init from parent and then custom 
        super().__init__(name, age)
        self.color = color


dog = Dog("nelly", 4)
cat = Cat("finn", 4)
fish = Fish("nemo", 2, "orange")

dog.speak()
cat.speak()