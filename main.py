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
        warnings.simplefilter("ignore")
        printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
        printVar.cPrint("[bold cyan3]Would you like to add more recipes([yellow]1[/]), look for recipes using your ingredients ([yellow]2[/]), edit a recipe ([yellow]3[/]), or view your Dishify ([yellow]4[/])?[/]")
        printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
        user = functions.getInput()
        if(user == "1"): #Add Recipes Into MYSQL ✔
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            printVar.cPrint("[bold cyan3]Please enter the name of the recipe file. We only support csvs in the format ID, Name, Ingredients!")
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            user = functions.getInput() 
            recipesDf = loadCsv.getRecipes(user)
            sql.createRecipe()
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            printVar.cPrint("[bold green3]Processing recipe data and pushing it to MySQL Server...")
            sql.fillRecipes(recipesDf)
            printVar.cPrint("[bold green3]Successfully uploaded to MySQL Server ✅")
            printVar.cPrint("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
        elif(user == "2"): #Search for Recipes using the ingredients ❌
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            printVar.cPrint("[bold cyan3]Would you like to do a quick search ([yellow]1[/]) or use your ingredients table? ([yellow]2[/])")
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            user = functions.getInput()
            if(user == "1"): 
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                printVar.cPrint("[bold cyan3]Enter your ingredients in the format: [yellow]ingredient,ingredient,ingredient[/] try to be as specific as possible!")
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                user = functions.getInput()
                recipes_using_ingredients = sql.getRecipesUsing(functions.cleanIngred(user))
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                printVar.tablePrint(recipes_using_ingredients, f"Recipes using [light_steel_blue]{user}")
                printVar.cPrint("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
        elif(user == "3"): #Editing Recipes / Del Recipes ✔
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            printVar.cPrint("[bold cyan3]Editing Recipe Screen")
            printVar.cPrint("[bold cyan3]Please enter the [yellow]Recipe ID (INT)[/] for the recipe you wish to edit")
            printVar.cPrint("[bold cyan3]If you do not know the Recipe ID you can also search recipes using ingredients in the format: [yellow]ingredient,ingredient,ingredient[/] 🤔")
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            recipeId = ""
            user = functions.getInput()
            #Getting RECIPE ID WORKING ✔
            if(user.isdigit()):
                recipeId = user
            else:
                recipes_using_ingredients = sql.getRecipesUsing(functions.cleanIngred(user))
                print(recipes_using_ingredients)
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                printVar.cPrint("[bold cyan3]What is the recipe ID that you are targeting?[/]")
                user = functions.getInput()
                recipeId = user
            printVar.cPrint("[bold cyan3]Recipe ID received! Would you like to edit ([yellow]1[/]) or delete ([yellow]2[/])")
            printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            user = functions.getInput()
            if(user == "1"): #UPDATE WORKING ✔
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                printVar.cPrint("[bold cyan3]Would you like to update the recipe name ([yellow]1[/]) or the recipe ingredients ([yellow]2[/])")
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                user = functions.getInput()
                if(user == "1"):
                    printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                    printVar.cPrint("[bold cyan3]Please enter the new recipe name")
                    printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                    user = input()
                    sql.updateName(recipeId, user)
                elif(user == "2"):
                    printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                    printVar.cPrint("[bold cyan3]Please enter the new recipe ingredients, be as concise as possible and include some instructtions if desired")
                    printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                    user = input()
                    sql.updateName(recipeId, user)
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                printVar.cPrint("[bold green3]Update completed! ✅")
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
            elif(user == "2"): #DELETE WORKING ✔
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
                printVar.cPrint(f"[bold green3]Deleting recipe with ID {recipeId}..")
                sql.deleteRecipe(recipeId)
                printVar.cPrint(f"[bold green3]Successfully Deleted ✅")
                printVar.cPrint("[bold white]----------------------------------------------------------------------------------------------------------------------------------")
        elif(user == "4"): #DISHIFY ❌
            pass
        else:
            printVar.cPrint("[bold red]Invalid Choice! Exiting ❌")
    elif(user != "1"):
        printVar.cPrint("[bold orange1]Please Enter 1 to Start the Program or Exit to exit the program.[/]")
    user = functions.getInput()

