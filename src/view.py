from rich.console import Console
from rich import print
console = Console()

import pyfiglet



class render():
    def render_info(self, obj):  
        if len(obj.selectedFiles) == 0: 
            # if selected files are less than 0, return print and reset value to default. IT WORKS SYNCHORNOUSLY
            console.print("[red]Warn: No images found to convert to png[/]\n[yellow]Try Again.[/]")
            console.print(f"Total scanned files: {obj.files_scanned}")
            
        else:
            console.print("[green]Images found")
            console.print(f"Total selected files: {obj.files_selected}")
            console.print(f"Total skipped files: {obj.files_skipped}")


def text_art():
    """
    Welcoming text artwork in ASCII. Requires pyfiglet
    """
    text = pyfiglet.figlet_format("Image Converter", font = "slant")
    console.print(f"[blink]{text}[/]")
    
    print("Made by [blue][link=https://www.twitter.com/Black_2_white]@Black_2_white[/link][/]!")
