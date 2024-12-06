# '''Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is'''
calculate_area = lambda base, height: (1/2)*base*height
print(calculate_area(2,10))

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is
rectangle_area = lambda length,width: length*width
print(rectangle_area(2,10))


# If no shape is supplied then it should take triangle as a default shape
# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

def print_pattern(height:int, width:int=None, shape="triangle"):
    if shape=="triangle":
        for i in range(1,height+1):
            print("*"*i)
    elif shape=="rectangle":
        try:
            for i in range(1,height+1):
                print("* "*width)
        except Exception as e:
            print(e,"\n width cant be empty or anything other then int")
        

print_pattern(height=5)
