class AdultException(Exception):
    pass

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_minar_age(self):
        if int(self.age) >= 18:
            raise AdultException
        else:
            return self.age
        
    def display(self):
        try:
            print(f"age -> {self.get_minar_age()}")
        except AdultException:
            print("Person is an Adult")
        finally:
            print(f"name -> {self.name}")


Person("someone",14).display()
Person("kalyan", 21).display()