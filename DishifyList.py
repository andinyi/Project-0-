import mysql.connector
import pandas as pd

import connector
import RecipeConnect

class Dishify(RecipeConnect.recipe_connector):
    def createDishify(self):
        self.cur.execute("USE recipes")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Dishify (`dishifyId` INT NOT NULL AUTO_INCREMENT, `RecipeID` INT, `Recipe Name` TEXT, `Ingredients` TEXT, `Instructions` TEXT, PRIMARY KEY (`dishifyID`), FOREIGN KEY (`RecipeID`) REFERENCES recipes(`ID`) ON UPDATE CASCADE ON DELETE CASCADE)")
    
    def showDishify(self):
        self.cur.execute("USE recipes")
        query = "SELECT * FROM Dishify"
        df = pd.read_sql(query, self.con)
        return df
    
    #takes a list object
    def addToDishify(self, recipeId):
        self.cur.execute("USE recipes")
        query = f'INSERT INTO Dishify (`RecipeID`, `Recipe Name`, `Ingredients`, `Instructions`) SELECT * FROM recipes WHERE `ID` = {recipeId}'
        self.cur.execute(query)
        self.con.commit()

    def updateNameDishify(self, RecipeId, string): #UPDATE
        self.cur.execute("USE recipes")
        query = f"""UPDATE dishify SET `Recipe Name` = "{string}" WHERE `dishifyId` = {RecipeId}"""
        self.cur.execute(query)
        self.con.commit()
    
    def updateIngredientsDishify(self, RecipeId, string): #UPDATE
        self.cur.execute("USE recipes") 
        query = f"""UPDATE dishify SET `Ingredients` = "{string}" WHERE `dishifyId` = {RecipeId}"""
        self.cur.execute(query)
        self.con.commit()
    
    def deleteRecipeDishify(self, RecipeId): #DELETE
        self.cur.execute("USE recipes")
        query = f"DELETE FROM dishify WHERE `dishifyId` = {RecipeId}"
        self.cur.execute(query)
        self.con.commit()