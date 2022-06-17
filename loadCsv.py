import pandas as pd

#LOADS CSV -> Python (Then Moves the Data into MYSQL if needed)
def getRecipes(recipecsv):
    data = pd.read_csv(recipecsv)
    data = data.dropna()
    return(data)
