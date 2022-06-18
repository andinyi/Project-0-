import pandas as pd
from rich import print
from rich.console import Console
from rich.text import Text
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table 

class printing():

    def __init__(self):
        self.console = Console()

    def printStart(self):
        panel = Panel("Hello!",title="[bold orange1]Andy's Recipe Book![/]", title_align="center", subtitle="[bold light_steel_blue]A Small Productivity Tool for Cooking[/]")
        self.console.print(panel)
        '''
        self.console.print("###############################################################", style="bold salmon1")
        self.console.print("###############################################################", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("####           [bold indian_red]WELCOME TO ANDY'S RECIPE BOOK![/]              ####", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("####       [light_coral]A Small Productivity Tool for Cooking[/]           ####", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("####          [green] Enter ([yellow]1[/]) to Start the Program [/]             ####", style="bold salmon1")
        self.console.print("####       [red] Type ([yellow]exit[/]) anytime to end the Program [/]        ####", style="bold salmon1")
        self.console.print("####      [grey93]A yellow color depicts choosable inputs![/]         ####", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("####                                                       ####", style="bold salmon1")
        self.console.print("###############################################################", style="bold salmon1")
        self.console.print("###############################################################", style="bold salmon1")
        '''

    def cPrint(self, string):
        self.console.print(string)

    def tablePrint(self, df, tableName):
        table = Table(title=tableName, style="bright_black")
        table.show_lines = True
        for i in df:
            if(i == "Ingredients"):
                table.add_column(i, style="white")
            else:
                table.add_column(i, style="orange1")
        if("ID" in df.columns):
            df["ID"] = pd.Series(df['ID'], dtype="string")
        for index, row in df.iterrows():
            table.add_row(*(row))
        self.console.print(table)
