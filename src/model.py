import os

from rich.console import Console

console = Console()

class model():
    def __init__(self):
        self.files_scanned = 0
        self.files_selected = 0
        self.files_skipped = 0
        self.selectedFiles = []
        
            
        
    def scan_dir(self, target_dir):
        
        try:
            """
            scan of the directory
            """      

            for file in os.listdir(target_dir):
                self.files_scanned+=1
                if os.path.splitext(file)[1] == ".jpg":  # check if it's a jpg
                    self.selectedFiles.append(file)
                    self.files_selected+=1
                else: # file is not jpg, then skip
                    self.files_skipped+=1
                    pass
            print(self.files_scanned)
        except FileNotFoundError:
            return True
    
    
    # Create a function that has a default arg value of none 
    # it will be used to save the images based in the directory
    
    def savingImgDir():
        pass
        
