import pandas as pd

#  My code
def poem_reader():
    poem = open("Assets/poem.txt", "r")
    poem = poem.read()
    sims = {",",";",":",".","!","\n","—"}
    for sim in sims:
    	poem = poem.replace(sim,"")
    List = poem.split(" ")

    def most_frequent(List:list):
        return max(set(List), key=List.count)

    print(most_frequent(List))





def stock_model():
    stock_data = pd.read_csv("Assets/stocks.csv")
    stock_data["PE Ratio"] = (stock_data["Price"]/stock_data["Earnings Per Share"]).round(2)
    stock_data["PB Ratio"] = (stock_data["Price"]/stock_data[" Book Value"]).round(2)
    model = stock_data[["Company Name","PE Ratio","PB Ratio"]]
    model.to_csv("Assets/output.csv",index=False)

poem_reader()
