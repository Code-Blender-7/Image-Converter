from rich.console import Console
from rich import print
from rich.progress import Progress
from time import sleep

console = Console()


import pyfiglet



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
 
    
    def error_DirMsg(self):
        """
        returns a captured rich error message. See Page 17 of the rich doc

        Returns:
            str: Error message
        """
        with console.capture() as capture:
            console.print(f"[red]WARN:[/] Directory invalid or False Input.\n\nPlease Try again.")
        return capture.get()


    def error_DirNotExist(self):
        """
        if directory doesn't exist
        """
        with console.capture() as capture:
            console.print("[red]WARN:[/] Directory does not exist or not found. Please Try again.")
        return capture.get()


    def enter_TargetDirMsg(self):
        return ("Enter the directory you want to convert the files: ")
    
    
    def renderingConvert(self, func):
        
        def convert():
            with console.screen() as screen:
                func()
        return convert



class CustomException(Exception):
    def __init__(self, exceptionType, code):
        self.exceptionType = exceptionType
        self.code = code
        print("Received: ", self.exceptionType, self.code)
        self.exceptionHandler()
    


    def exceptionHandler(self):
        if self.exceptionType == KeyboardInterrupt and self.code == 101: self.keyBoardErrorMsg()
        elif self.exceptionType == KeyboardInterrupt and self.code == None: self.keyBoardErrorMsg_IN_PROCESS()
        elif self.exceptionType == KeyboardInterrupt and self.code == 105: self.abortWhileConvert()
        else: 
            print("Expection Message of this catagory doesn't exist")
            print(self.exceptionType)
    
    
    def keyBoardErrorMsg(self):
        console.print("\n[red]User Aborted Proces")
    
    def keyBoardErrorMsg_IN_PROCESS(self):
        console.print("\n[red]User Aborted Proces while in operations")
    
    def abortWhileConvert(self):
        console.print("\n[on red]WARNING[/]. Program force-exit over converting process. Chances of corrupt-files is possible.")
        


def text_art():
    """
    Welcoming text artwork in ASCII. Requires pyfiglet
    """
    text = pyfiglet.figlet_format("Image Converter", font = "slant")
    console.print(f"[blink]{text}[/]")
    
    print("Made by [blue][link=https://www.twitter.com/Black_2_white]@Black_2_white[/link][/]!")
    
        
