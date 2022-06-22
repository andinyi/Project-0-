#Recipe Searching and Suggestions
from DishifyList import Dishify
import RecipeConnect as rc
from Ingredients import ingredientsTable
import functions
import loadCsv
from printing import printing

import pandas as pd
from dotenv import load_dotenv
import os
import warnings


load_dotenv("ID.env")

sql = ingredientsTable(os.getenv("user"), os.getenv("pass"), "localhost")

printVar = printing()
printVar.printStart()
user = functions.getInput() #function to get input and clean the input



while(user != "exit"):
    if(user == "1"):
        warnings.simplefilter("ignore")
        printVar.printPanel("[bold cyan3]Would you like to add more recipes ([yellow]1[/]), look for recipes using your ingredients ([yellow]2[/]), edit a recipe ([yellow]3[/]), view your Dishify ([yellow]4[/]), or view a saved table? ([yellow]5[/])?[/]")
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
                printVar.printPanel("[bold cyan3]Currently fetching your ingredients...")
                sql.createIngredientsTable()
                printVar.tablePrintNoBar(sql.showIngredients(), "[bold orange1]Your ingredients")
                printVar.printPanel("[bold cyan3]Would you like to add ([yellow]1[/]) or edit ([yellow]2[/]) your ingredients? You can also search using this table ([yellow]3[/])")
                user = functions.getInput()
                if(user == "1"):
                    printVar.printPanel("[bold cyan3]Please enter the [yellow]ingredient,ingredient,ingredient[/] format you would like the add to your ingredients list.")
                    user = functions.getInput()
                    sql.addToIngredients(functions.cleanIngred(user))
                    printVar.printPanel("[bold green]Successfull added ingredient!")
                elif(user == "2"):
                    printVar.printPanel("[bold cyan3]Please enter the [yellow]ingredient id[/] of the ingredient you would like to edit.")
                    user = functions.getInput()
                    if(user == "exit"):
                        break
                    if(user.isdigit()):
                        ingredientID = user
                    else:
                        printVar.printPanel("[bold red]ID is wrong format! Exiting!")
                        break
                    printVar.printPanel("[bold cyan3]ID received! Would you like to edit ([yellow]1[/]) or delete ([yellow]2[/])")
                    user = functions.getInput()
                    if(user == "1"): #UPDATE WORKING ✔
                        printVar.printPanel("[bold cyan3]Please enter the [yellow]ingredient[/] to be added!")
                        user = functions.getInput()
                        sql.updateIngredient(ingredientID, user)
                        printVar.printPanel("[bold green3]Update completed!")
                    elif(user == "2"): #DELETE WORKING ✔
                        sql.deleteIngredient(ingredientID)
                        printVar.printPanel(f"[bold green3]Deleting ingredient with ID {ingredientID}..\n" +
                                             "[bold green3]Successfully Deleted!")
                    elif(user == "exit"):
                        break
                elif(user == "3"):
                    printVar.printPanel("[bold cyan3]Grabbing all recipes that use your ingredients")
                    tmp = sql.getIngredients()
                    tmpDf = sql.getRecipesUsing(tmp)
                    printVar.tablePrintNoBar(tmpDf, "[bold orange1]Recipes using your ingredients!")
                    printVar.printPanel("[bold cyan3]Would you like to save this table? [yellow]yes[/] or [yellow]no[/]?")
                    user = functions.getInput()
                    if(user == "yes"):
                        printVar.printPanel("[bold cyan3]Enter the [yellow]name[/] you wish to give to the table")
                        user = functions.getInput()
                        sql.SaveTable(tmpDf, user)
                        printVar.printPanel(f"[bold cyan3]Successfully created the table {user}")
                    elif(user == "no"):
                        printVar.printPanel(f"[bold cyan3]Understood!")
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
                printVar.printPanel("[bold green3]Update completed!")
            elif(user == "2"): #DELETE WORKING ✔
                sql.deleteRecipe(recipeId)
                printVar.printPanel(f"[bold green3]Deleting recipe with ID {recipeId}..\n" +
                                     "[bold green3]Successfully Deleted!")
            elif(user == "exit"):
                break
            printVar.printPanel("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
        elif(user == "4"): #DISHIFY ✅
            printVar.printPanel("[bold cyan3]Currently fetching your Dishify...")
            sql.createDishify()
            printVar.tablePrintNoBar(sql.showDishify(), "[bold orange1]Your Dishify")
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
                        if(user == "exit"):
                            break
                        sql.updateNameDishify(recipeId, user)
                    elif(user == "2"):
                        printVar.printPanel("[bold cyan3]Please enter the new recipe ingredients, be as concise as possible and include some instructtions if desired")
                        user = input()
                        if(user == "exit"):
                            break
                        sql.updateIngredientsDishify(recipeId, user)
                    elif(user == "exit"):
                        break
                    printVar.printPanel("[bold green3]Update completed!")
                elif(user == "2"): #DELETE WORKING ✔
                    sql.deleteRecipeDishify(recipeId)
                    printVar.printPanel(f"[bold green3]Deleting recipe with ID {recipeId}.." +
                                         "[bold green3]Successfully Deleted!")
                elif(user == "exit"):
                    break
            elif(user == "exit"):
                break
            printVar.printPanel("[bold green3]Successfully updated to Dishify!")
            printVar.printPanel("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
        elif(user == "5"):
            printVar.printPanel("[bold cyan3]Please enter the table name! Case sensitive")
            user = functions.getInput()
            printVar.tablePrint(sql.viewTable(user), f"[bold orange1]{user}")
            printVar.printPanel("[bold cyan3]Moving back to main prompt, Enter 1 to continue")
        elif(user == "exit"):
            break
        else:
            printVar.printPanel("[bold red]Invalid Choice! Exiting ❌")
    elif(user != "1"):
        printVar.printPanel("[bold orange1]Please Enter 1 to Start the Program or Exit to exit the program.[/]")
    user = functions.getInput()

