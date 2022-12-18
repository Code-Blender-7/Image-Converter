from rich.console import Console
from rich import print
console = Console()

import pyfiglet



class render():
    def __init__(self, ModelClassData):
        self.classData = ModelClassData
        
        
    def render_info(self):  
        console.print("[green]Images found")
        console.print(f"Total selected files: {self.classData.files_selected}")
        console.print(f"Total skipped files: {self.classData.files_skipped}")

    def exceptionHandlings(self, exceptionType):
        if exceptionType == "FileNotFoundError": console.print("Error found. This file doesn't exist")


    def render_NO_FILES(self):
        console.print("[red]Warn: No images found to convert to png[/]\n[yellow]Try Again.[/]")
        console.print(f"Total scanned files: {self.classData.files_scanned}")
        console.print(f"Found to convert: [red]{self.classData.files_selected}[/]\n")



def text_art():
    """
    Welcoming text artwork in ASCII. Requires pyfiglet
    """
    text = pyfiglet.figlet_format("Image Converter", font = "slant")
    console.print(f"[blink]{text}[/]")
    
    print("Made by [blue][link=https://www.twitter.com/Black_2_white]@Black_2_white[/link][/]!")
