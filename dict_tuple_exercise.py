import numpy as np

class population_index_handler():
    def __init__(self):
        self.population_index = {"China":143,"india":136,"USA":32,"Pakistan":21}
        self.command = input("Enter your comand: ")
        if self.command=="print":
            self.print_database()
        elif self.command=="add":
            new_county = input("Pleaase enter county name: ")
            if new_county in self.population_index.keys():
                print("county allrady exist in the data set")
            else:
                new_population = input(f"Please enter the {new_county}'s population: ")
                self.population_index[new_county] = new_population
                self.print_database()
        elif self.command=="remove":
            rm_county = input("Please enter the county name: ")
            if rm_county not in self.population_index.keys():
                print("Country don't exist in the database")
            else:
                self.population_index.pop(rm_county)
                self.print_database()
        elif self.command=="quary":
            q_county = input("Please enter the name of the country: ")
            if q_county not in self.population_index.keys():
                print("Country don't exist in the database")
            else:
                print(f"Population: {self.population_index[q_county]}")
        else:
            print("Invalid Command you are only allowed to perfome\n   1) print\n   2) add\n   3) remove\n   4) quary")


    def print_database(self):
        for key in self.population_index.keys():
            print(f"{key}==>{self.population_index[key]}")


class AVG_price():
    def __init__(self):
        self.data = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
        self.oprations = input("\n\nPlease Define your oppration: ")
        if self.oprations == "print":
            self.print_data()
        elif self.oprations == "add":
            stock_ticker = input("please enter the stock ticker: ")
            prices = input("please enter the amount: ")
            if stock_ticker in self.data.keys():
                self.data[stock_ticker].append(float(prices))
                self.print_data()
            else:
                self.data[stock_ticker] = [float(prices)]
                self.print_data()

        else:
            print("Not a valid opration you are only allowed to perfome\n   1) print\n   2) add")
    def print_data(self):
        Avg = lambda prices: round(np.array(prices).prod()**(1/len(prices)),2) # Geyomatric mean/AVG method
        # Avg = lambda prices: round(np.mean(prices),2)
        for key in self.data.keys():
            print(f"{key} ==> {self.data[key]} ==> avg:  {Avg(self.data[key])}")

class Circle_Calc():
    def circle_calc(radious):
        area = round(np.pi * (radious ** 2), 2)
        circumference = round(2 * np.pi * radious, 2)
        diameter = round(2 * radious, 2)
        return area, circumference, diameter
    
if __name__=="__main__":
    population_index_handler()
    AVG_price()
    try:
        radious = float(input("\n\nEnter the radious of the circle: "))
        area, circumference, diameter = Circle_Calc.circle_calc(radious)
        print(f"area of circle: {area}")
        print(f"circumference of circle: {circumference}")
        print(f"diameter of circle: {diameter}")
    except Exception as e:
        print(e,"\n", "only accept value in float or intiger")
