class Employee():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def output(self):
        print(f"Employ ID id {self.id} and Name is {self.name}\n")

emp = Employee(1, "coder")
emp.output()

del emp.id
try:
    print(emp.id)
except Exception as e:
    print(e)

del emp.name
try:
    print(emp.name)
except Exception as e:
    print(e)