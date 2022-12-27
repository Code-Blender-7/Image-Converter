from rich.console import Console
from rich.progress import Progress
from rich.prompt import Confirm
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, TransferSpeedColumn

import pyfiglet


console = Console()
confirm = Confirm()


progress = Progress(
    SpinnerColumn(),
    *Progress.get_default_columns(), # get default settings
    "Elapsed:", TimeElapsedColumn(), # this is a slacked display. Read Docs of Rich before making changes.
    transient=True # clear progress bar + others after completion/end
    )


class render():
    def __init__(self, ModelClassData):
        self.classData = ModelClassData
        
        
    def render_info(self):  
        console.print("[green]Images found")
        console.print(f"Total selected files: {self.classData.files_selected}")
        console.print(f"Total skipped files: {self.classData.files_skipped}")


    def render_NO_FILES(self):
        console.print("[red]Warn: No images found to convert to png[/]\n[yellow]Try Again.[/]")
        console.print(f"Total scanned files: {self.classData.files_scanned}")
        console.print(f"Found to convert: [red]{self.classData.files_selected}[/]\n")


    def insert_SavingDirMsg(self):
        return ("Insert 'new' folder location to save converted files : ")
    

    def error_DirNotExist(self):
        """
        if directory doesn't exist
        """
        with console.capture() as capture:
            console.print("[on red]WARNING:[/] Directory does not exist or not found. \nPlease Try again.")
        return capture.get()


    def enter_TargetDirMsg(self):
        return ("\nEnter the directory you want to convert the files: ")
    
    
    def convertCompleteResults(self):
        console.print(f"\nTotal Converted: [green]{self.classData.files_converted}\nConverted files saved directory[/]: [blink2][i]{self.classData.savingDir}")
    
    
    def DirNotFoundWarning(self):
        """
        returns a captured rich error message. See Page 17 of the rich doc

        Returns:
            str: Error message
        """
        with console.capture() as capture:
            console.print("[on red]WARNING:[/] Directory does not exist or not found.")
        return capture.get()
    

    def text_art(self):
        """
        Welcoming text artwork in ASCII. Requires pyfiglet
        """
        text = pyfiglet.figlet_format("Image Converter", font = "slant")
        console.print(f"[blink]{text}[/]")

        console.print("Made by [blue][link=https://www.twitter.com/Black_2_white]@Black_2_white[/link][/]!")
        

    def filePlacementChoiceDisplay(self):
        console.rule("CONVERTING MODE")
        choice = confirm.ask("\nSave files in another directory? (y)\nSave files in current Directory (n)")
        return choice
    

class CustomException(Exception):
    
    def __init__(self, exceptionType, code=None):
        self.exceptionType = exceptionType
        self.code = code
        self.exceptionHandler()
    


    def exceptionHandler(self):
        if self.exceptionType == KeyboardInterrupt and self.code == 101: self.keyBoardErrorMsg()
        elif self.exceptionType == KeyboardInterrupt and self.code == 105: self.abortWhileConvert()
        elif self.exceptionType == EOFError: self.EOFErrorHandler()
        else: 
            console.print("Expection Message of this catagory doesn't exist")
            console.print(self.exceptionType)
    
    
    def keyBoardErrorMsg(self):
        console.print("\n[red]User Aborted Proces")
    
    
    def abortWhileConvert(self):
        console.print("\n\n[on red]WARNING[/]. Program force-exit over converting process. Chances of corrupt-files is possible.\n")

        
    def EOFErrorHandler(self):
        console.print("\n[on red][blink2]OOPS[/][/]. The given input was not valid. Please try again.")
        
