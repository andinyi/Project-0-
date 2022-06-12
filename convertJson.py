import pandas as pd 
import json 

#converts Json With Name -> Dataframe
def returnDataframe(jsonFileName): 
    with open(jsonFileName) as file:
        posts = json.load(file)

    df = pd.DataFrame(posts)

    print(f"\033[93m {df}\033[00m")

    jsonFileName = jsonFileName.replace('.json', '')

    df = df[jsonFileName]
    newDf = pd.DataFrame()
    for i in range(df.count()):
        tmp = pd.DataFrame.from_dict(df[i])
        newDf = pd.concat([newDf, tmp], ignore_index=True)
    
    if("tags" in newDf):
        newDf = newDf.drop(columns="tags")

    if("images" in newDf):
        newDf = newDf.drop(columns="images")  
    
    newDf = newDf.drop_duplicates()

    return newDf


out = returnDataframe("posts.json")
print(f"\033[92m {out}\033[00m")