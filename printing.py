from click import style
from rich import print
from rich.console import Console
from rich.text import Text
from rich.layout import Layout
from rich.panel import Panel

class printing():

    def __init__(self):
        self.console = Console()

    def printStart(self):
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

    def cPrint(self, string):
        self.console.print(string)
