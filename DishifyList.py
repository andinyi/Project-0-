import mysql.connector
import pandas as pd

import connector
import RecipeConnect

class Dishify(RecipeConnect.recipe_connector):
    def createDishify(self):
        self.cur.execute("USE recipes")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Dishify (`dishifyId` INT NOT NULL AUTO_INCREMENT, `RecipeID` INT, `Recipe Name` TEXT, `Ingredients` TEXT, PRIMARY KEY (`dishifyID`), FOREIGN KEY (`RecipeID`) REFERENCES recipes(`ID`))")
    
    def showDishify(self):
        query = "SELECT * FROM Dishify"
        df = pd.read_sql(query, self.con)
    
    #takes a list object
    def addToDishify(self, series):
        query = 'INSERT INTO Dishify (`RecipeID`, `Recipe Name`, `Ingredients`) VALUES (%s, %s, %s)'
        arg = [int(series[0]), series[1], series[2]]
        self.cur.execute(query, arg)
        self.con.commit()

