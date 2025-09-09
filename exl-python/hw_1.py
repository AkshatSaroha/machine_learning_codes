# class Vehicle:
#     def start(self):
#         print("Broom Broom !!!")

# class Car(Vehicle):
#     def honk(self):
#         print("Pee Pee Poo Poo")

# my_car = Car()

# my_car.start()
# my_car.honk()  



# class Chef:
#     def cook(self):
#         print("Cooking food")

# class Driver:
#     def drive(self):
#         print("Driving vehicle")

# class Person(Chef, Driver):
#     def work(self):
#         print("Working multitask")

# person1 = Person()

# person1.cook() 
# person1.drive() 
# person1.work()  


# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("Barking")

# class Puppy(Dog):
#     def play(self):
#         print("Playing")

# puppy1 = Puppy()

# puppy1.eat()  
# puppy1.bark() 
# puppy1.play() 



# class Device:
#     def power_on(self):
#         print("Powering on")

# class Laptop(Device):
#     def code(self):
#         print("Coding on laptop")

# class Smartphone(Device):
#     def call(self):
#         print("Making a call")

# laptop1 = Laptop()
# laptop1.power_on()  
# laptop1.code()      

# phone1 = Smartphone()
# phone1.power_on()  
# phone1.call()      


class Employee:
    def work(self):
        print("Working")

class Engineer(Employee):
    def design(self):
        print("Designing")

class Manager(Employee):
    def manage(self):
        print("Managing")

class TechLead(Engineer, Manager):
    def lead(self):
        print("Leading the team")

lead1 = TechLead()

lead1.work()     
lead1.design()  
lead1.manage()   
lead1.lead()    
