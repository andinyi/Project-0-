import mysql.connector
import pandas as pd

import connector
import RecipeConnect
import DishifyList

class ingredientsTable(DishifyList.Dishify):
    def createIngredientsTable(self):
        self.cur.execute("USE recipes")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ingredients (`ingredientID` INT NOT NULL AUTO_INCREMENT, ingredient TEXT, PRIMARY KEY (`ingredientID`))")
    
    def showIngredients(self):
        self.cur.execute("USE recipes")
        query = "SELECT * FROM ingredients"
        df = pd.read_sql(query, self.con)
        return df
    
    def addToIngredients(self, ingredientName):
        self.cur.execute("USE recipes")
        for i in ingredientName:
            query = f'INSERT INTO ingredients (`ingredient`) VALUES ("{i}")'
            self.cur.execute(query)
        self.con.commit()

    def updateIngredient(self, id, string): #UPDATE
        self.cur.execute("USE recipes") 
        query = f"UPDATE ingredients SET `ingredient` = '{string}' WHERE `ingredientID` = {id}"
        self.cur.execute(query)
        self.con.commit()

    def deleteIngredient(self, id): #DELETE
        self.cur.execute("USE recipes")
        query = f"DELETE FROM ingredients WHERE `ingredientID` = {id}"
        self.cur.execute(query)
        self.con.commit()