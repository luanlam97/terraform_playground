import pandas as pd
def add(x = 1, y = 2):
    output =  x + y
    return pd.DataFrame([output]) 




if __name__ == "__main__":
    print(add(1,2).values[0][0])