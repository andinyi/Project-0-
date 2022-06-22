import mysql.connector
import pandas as pd
import functions

import connector

class recipe_connector(connector.Connector):

    def createRecipe(self):  #CREATE
        self.cur.execute("CREATE DATABASE IF NOT EXISTS recipes")
        self.cur.execute("USE recipes")

    def fillRecipes(self, df): #CREATE
        self.cur.execute("USE recipes")
        self.cur.execute("CREATE TABLE IF NOT EXISTS recipes (`ID` INT NOT NULL AUTO_INCREMENT, `Recipe Name` TEXT, `Ingredients` TEXT, `Instructions` TEXT, PRIMARY KEY(`ID`))")
        query = """INSERT INTO recipes (`Recipe Name`, `Ingredients`, `Instructions`) VALUES (%s, %s, %s)"""
        
        for index, row in df.iterrows():
            arg = [row[0], row[1], row[2]]
            self.cur.execute(query, arg)
            functions.printProgressBar(index + 1, len(df))

        self.con.commit()

    def getRecipesUsing(self, desiredIngredients): #READ
        self.cur.execute("USE recipes")
        query = "SELECT `ID`, `Recipe Name`, `Ingredients` FROM recipes WHERE"
        for i, ingredient in enumerate(desiredIngredients):
            ingredient = ingredient.replace(" ", "")
            if(i == 0):
                query = query + f' LOCATE ("{ingredient}", `Ingredients`) > 0'
            else:
                query = query + f' AND LOCATE ("{ingredient}", `Ingredients`) > 0'
    
        df = pd.read_sql(query, self.con)
        return df

    def updateName(self, RecipeId, string): #UPDATE
        self.cur.execute("USE recipes")
        query = f"""UPDATE recipes SET `Recipe Name` = "{string}" WHERE `ID` = {RecipeId}"""
        self.cur.execute(query)
        self.con.commit()
    
    def updateIngredients(self, RecipeId, string): #UPDATE
        self.cur.execute("USE recipes") 
        query = f"""UPDATE recipes SET `Ingredients` = "{string}" WHERE `ID` = {RecipeId}"""
        self.cur.execute(query)
        self.con.commit()
    

    def deleteRecipe(self, RecipeId): #DELETE
        self.cur.execute("USE recipes")
        query = f"DELETE FROM recipes WHERE `ID` = {RecipeId}"
        self.cur.execute(query)
        self.con.commit()

    def SaveTable(self, df, name):
        self.cur.execute("USE recipes")
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS `{name}` (`Recipe ID` INT, `Recipe Name` TEXT, `Ingredients` TEXT, FOREIGN KEY(`Recipe ID`) REFERENCES recipes(`ID`))")
        query = f"""INSERT INTO `{name}` (`Recipe ID`, `Recipe Name`, `Ingredients`) VALUES (%s, %s, %s)"""
        
        for index, row in df.iterrows():
            arg = [row[0], row[1], row[2]]
            self.cur.execute(query, arg)
        
        self.con.commit()
    
    def viewTable(self, name):
        self.cur.execute("USE recipes")
        query = f"""SELECT * FROM `{name}`"""
        df = pd.read_sql(query, self.con)
        return df