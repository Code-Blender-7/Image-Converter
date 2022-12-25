
from rich.console import Console 


console = Console()

class ExceptionHandler(Exception):
    def __init__(self, exceptionType, code):
        self.exceptionType = exceptionType
        self.code = code
        self.exceptionHandler()

    def exceptionHandler(self):
        if self.exceptionType == KeyboardInterrupt and self.code == 101: self.keyBoardErrorMsg()
        if self.exceptionType == KeyboardInterrupt and self.code == None: self.keyBoardErrorMsg_IN_PROCESS()
    
    
    def keyBoardErrorMsg(self):
        console.print("[red]User Aborted Proces")
    
    def keyBoardErrorMsg_IN_PROCESS(self):
        console.print("[red]User Aborted Proces while in operations")

try:
    raise(ExceptionHandler(exceptionType=KeyboardInterrupt, code=None))
except Exception:
    pass