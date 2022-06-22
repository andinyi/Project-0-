from ntpath import join
from numpy import dtype
import pandas as pd 
import pandasql as psql
import json 

#converts Json With Name -> Dataframe -> CSV
def returnDataframe(jsonFileName): 
    with open(jsonFileName) as file:
        named = json.load(file)

    df = pd.DataFrame(named)

    df = df.transpose()

    newDf = pd.DataFrame()
    
    newDf = pd.concat([newDf, df["title"]], axis=1, ignore_index=True)
    newDf = pd.concat([newDf, df["ingredients"]], axis=1, ignore_index=True)
    newDf = pd.concat([newDf, df["instructions"]], axis =1, ignore_index=True)

    newDf = newDf.reset_index(drop=True)
    newDf = newDf.dropna()

    newDf[1] = newDf[1].apply(lambda s : ",".join(s))
    newDf[1] = newDf[1].str.lower()

    query = 'SELECT "0" as "Recipe Name", "1" as Ingredients, "2" as Instructions FROM newDf'
    
    myDf = psql.sqldf(query)

    return myDf

#requires a dataframe and a csvName to run (makes a csvFile)
def toCsv(dataframe, csvName):
    pd.DataFrame.to_csv(dataframe, csvName)


toCsv(returnDataframe("recipes_fn.json"), "recipes_fn.csv")