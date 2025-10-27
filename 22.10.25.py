class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age     

    def say_hello(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет.")
        


person1 = Person("Айдана", 18)


person1.say_hello()
