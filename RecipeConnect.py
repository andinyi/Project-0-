import mysql.connector
import pandas as pd
import functions

import connector
import printing

class recipe_connector(connector.Connector):
    def createRecipe(self):
        self.cur.execute("CREATE DATABASE IF NOT EXISTS recipes")
        self.cur.execute("USE recipes")

    def fillRecipes(self, df):
        self.cur.execute("USE recipes")
        self.cur.execute("CREATE TABLE IF NOT EXISTS recipes (`ID` INT NOT NULL AUTO_INCREMENT, `Recipe Name` TEXT, `Ingredients` TEXT, PRIMARY KEY(`ID`))")
        query = 'INSERT INTO recipes (`Recipe Name`, `Ingredients`) VALUES (%s, %s)'
        for index, row in df.iterrows():
            arg = [row[0], row[1]]
            self.cur.execute(query, arg)
            functions.printProgressBar(index + 1, len(df))

        self.con.commit()

    def getRecipesUsing(self, desiredIngredients):
        self.cur.execute("USE recipes")
        query = "SELECT * FROM recipes WHERE"
        for i, ingredient in enumerate(desiredIngredients):
            if(i == 0):
                query = query + f' LOCATE ("{ingredient}", `Ingredients`) > 0'
            else:
                query = query + f' AND LOCATE ("{ingredient}", `Ingredients`) > 0'
    
        df = pd.read_sql(query, self.con)
        return df

    