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
        printVar.printPanel("[bold cyan3]Would you like to add more recipes ([yellow]1[/]), look for recipes using your ingredients ([yellow]2[/]), edit a recipe ([yellow]3[/]), or view your Dishify ([yellow]4[/])?[/]")
        user = functions.getInput()
        if(user == "1"): #Add Recipes Into MYSQL ✔  FIXED Console Prompts as well
            printVar.printPanel("[bold cyan3]Please enter the name of the recipe file. We only support csvs in the format ID, Name, Ingredients!")
            user = functions.getInput()
            if(user == "exit"):
                    break 
            recipesDf = loadCsv.getRecipes(user)
            sql.createRecipe()
            printVar.cPrint("[bold green3]Processing recipe data and pushing it to MySQL Server...")
            sql.fillRecipes(recipesDf)
            printVar.printPanel("[bold green3]Successfully uploaded to MySQL Server ✅[/]\n"
                            "[bold cyan3]Moving back to main prompt, Enter 1 to continue")
        elif(user == "2"): #Search for Recipes using the ingredients ❌
            printVar.printPanel("[bold cyan3]Would you like to do a quick search ([yellow]1[/]) or use your ingredients table? ([yellow]2[/])")
            user = functions.getInput()
            if(user == "1"): 
                printVar.printPanel("[bold cyan3]Enter your ingredients in the format: [yellow]ingredient,ingredient,ingredient[/] try to be as specific as possible!")
                user = functions.getInput()
                if(user == "exit"):
                    break
                recipes_using_ingredients = sql.getRecipesUsing(functions.cleanIngred(user))
                printVar.tablePrint(recipes_using_ingredients, f"Recipes using [light_steel_blue]{user}")
            elif(user == "2"):
                #Searching using Ingredients Table
                pass
            elif(user == "exit"):
                break
            printVar.printPanel("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
        elif(user == "3"): #Editing Recipes / Del Recipes ✔
            printVar.printPanel("[bold cyan3]Editing Recipe Screen\n" +
                                "Please enter the [yellow]Recipe ID (INT)[/] for the recipe you wish to edit\n" +
                                "If you do not know the Recipe ID you can also search recipes using ingredients in the format: [yellow]ingredient,ingredient,ingredient[/] 🤔"
                                )
            recipeId = ""
            user = functions.getInput()
            if(user == "exit"):
                    break
            #Getting RECIPE ID WORKING ✔
            if(user.isdigit()):
                recipeId = user
            else:
                recipes_using_ingredients = sql.getRecipesUsing(functions.cleanIngred(user))
                printVar.tablePrint(recipes_using_ingredients, f"Recipes using {user}")
                printVar.printPanel("[bold cyan3]What is the [yellow]recipe ID[/] that you are targeting? [yellow](exit)[/] to cancel and close the program [/]")
                user = functions.getInput()
                if(user == "exit"):
                    break
                recipeId = user
            printVar.printPanel("[bold cyan3]Recipe ID received! Would you like to edit ([yellow]1[/]) or delete([yellow]2[/])")
            user = functions.getInput()
            if(user == "1"): #UPDATE WORKING ✔
                printVar.printPanel("[bold cyan3]Would you like to update the recipe name ([yellow]1[/]) or the recipe ingredients ([yellow]2[/])")
                user = functions.getInput()
                if(user == "1"):
                    printVar.printPanel("[bold cyan3]Please enter the new recipe name")
                    user = input()
                    sql.updateName(recipeId, user)
                elif(user == "2"):
                    printVar.printPanel("[bold cyan3]Please enter the new recipe ingredients, be as concise as possible and include some instructtions if desired")
                    user = input()
                    sql.updateIngredients(recipeId, user)
                elif(user == "exit"):
                    break
                printVar.printPanel("[bold green3]Update completed! ✅")
            elif(user == "2"): #DELETE WORKING ✔
                printVar.printPanel(f"[bold green3]Deleting recipe with ID {recipeId}..")
                sql.deleteRecipe(recipeId)
                printVar.printPanel(f"[bold green3]Successfully Deleted ✅")
            elif(user == "exit"):
                break
        elif(user == "4"): #DISHIFY ❌
            printVar.printPanel("[bold cyan3]Currently fetching your Dishify...")
            sql.createDishify()
            printVar.tablePrint(sql.showDishify(), "[bold orange1]Your Dishify")
            printVar.printPanel("[bold cyan3]Would you like to add ([yellow]1[/]) or edit ([yellow]2[/]) your Dishify?")
            user = functions.getInput()
            if(user == "1"):
                printVar.printPanel("[bold cyan3]Please enter the [yellow]Recipe ID[/] of the recipe you would like the add to Dishify.")
                user = functions.getInput()
                sql.addToDishify(user)
            elif(user == "2"):
                printVar.printPanel("[bold cyan3]Please enter the [yellow]Dishify ID[/] of the recipe you would like to edit.")
                user = functions.getInput()
                if(user == "exit"):
                    break
                if(user.isdigit()):
                    recipeId = user
                else:
                    printVar.printPanel("[bold red]ID is wrong format! Exiting!")
                    break
                printVar.printPanel("[bold cyan3]Recipe ID received! Would you like to edit ([yellow]1[/]) or delete ([yellow]2[/])")
                user = functions.getInput()
                if(user == "1"): #UPDATE WORKING ✔
                    printVar.printPanel("[bold cyan3]Would you like to update the recipe name ([yellow]1[/]) or the recipe ingredients ([yellow]2[/])")
                    user = functions.getInput()
                    if(user == "1"):
                        printVar.printPanel("[bold cyan3]Please enter the new recipe name")
                        user = input()
                        sql.updateNameDishify(recipeId, user)
                    elif(user == "2"):
                        printVar.printPanel("[bold cyan3]Please enter the new recipe ingredients, be as concise as possible and include some instructtions if desired")
                        user = input()
                        sql.updateIngredientsDishify(recipeId, user)
                    elif(user == "exit"):
                        break
                    printVar.printPanel("[bold green3]Update completed! ✅")
                elif(user == "2"): #DELETE WORKING ✔
                    printVar.printPanel(f"[bold green3]Deleting recipe with ID {recipeId}..")
                    sql.deleteRecipeDishify(recipeId)
                    printVar.printPanel(f"[bold green3]Successfully Deleted ✅")
                elif(user == "exit"):
                    break
            elif(user == "exit"):
                break
            printVar.cPrint("[bold green3]Successfully updated to Dishify ✅")
            printVar.cPrint("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
        elif(user == "exit"):
            break
        else:
            printVar.cPrint("[bold red]Invalid Choice! Exiting ❌")
    elif(user != "1"):
        printVar.cPrint("[bold orange1]Please Enter 1 to Start the Program or Exit to exit the program.[/]")
    user = functions.getInput()

