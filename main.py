#Recipe Searching and Suggestions
from DishifyList import Dishify
import RecipeConnect as rc
import functions
import convertJson
import loadCsv
from printing import printing
import connector

import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
from rich.progress import track
import warnings


load_dotenv("ID.env")

sql = Dishify(os.getenv("user"), os.getenv("pass"), "localhost")

printVar = printing()
printVar.printStart()
user = functions.getInput() #function to get input and clean the input

while(user != "exit"):
    if(user == "1"):
        printVar.cPrint("[bold cyan3]Would you like to add more recipes ([yellow]1[/]) or look for recipes using your ingredients ([yellow]2[/]) ?.[/]")
        user = functions.getInput()
        if(user == "1"):
            warnings.simplefilter("ignore")
            printVar.cPrint("[bold cyan3]Please enter the name of the recipe file. We only support csvs in the format ID, Name, Ingredients!")
            user = functions.getInput() 
            recipesDf = loadCsv.getRecipes(user)
            sql.createRecipe()
            printVar.cPrint("[bold green3]Processing recipe data and pushing it to MySQL Server...")
            sql.fillRecipes(recipesDf)
            printVar.cPrint("[bold green3]Successfully uploaded to MySQL Server")

    elif(user != "1"):
        printVar.cPrint("[bold orange1]Please Enter 1 to Start the Program or Exit to exit the program.[/]")
    user = functions.getInput()




