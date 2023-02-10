
from rich.console import Console
from rich.panel import Panel
from time import sleep

# include Panels, console, Text
# Panel Page 55

console = Console()

def readme():
    text_INTRODUCTION = """
Image Converter is a Python Command Line Interface (CLI) utility tool used to convert all the images in a folder from JPG to PNG.  
"""

    text_USAGE = f"""
1. Insert a folder directory. The program will scan for potential JPG files. If it finds none, then the program will return with an error in search.

2. The Program will ask if you rather want to save the images inside the folder from where you are converting or to save them in a new directory.

3. If that directory doesn't exist, the program will prompt for creating new directory based on the previous input value.

4. The program after converting will show the after actions report of its recent convertion.
"""

    text_CAUTION = f"""
There are a lot of work left here to be done to make this project completed.
If you were to find any bugs, please open up an issue.
Also please don't change the size of your terminal because this is not responsive. 
    """

    console.print(Panel(f"[white]{text_INTRODUCTION}[/]",style="blue", title="Introduction"))
    console.print(Panel(f"[white]{text_USAGE}[/]",style="blue", title="Usage"))
    console.print(Panel(f"[white]{text_CAUTION}[/]",style="blue", title=":warning: [white on red]Caution[/] :warning:"))
    
    
