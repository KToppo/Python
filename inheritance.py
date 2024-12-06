class Animal():
    def __init__(self,Type):
    	self.type = Type
    	print(f"type {self.type} in animal class")

    def an(self):
        print(f"its a animal class of {self.type}")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
        print("It's dog class")


test = Dog()
test.an()
