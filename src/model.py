import os

from rich.console import Console

console = Console()

class model():
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.files_scanned = 0
        self.files_selected = 0
        self.files_skipped = 0
        self.selectedFiles = []
        self.scan_dir()
        
            
    def scan_dir(self):
        
        """
        scan of the directory
        """      

        for file in os.listdir(self.target_dir):
            self.files_scanned+=1
            if os.path.splitext(file)[1] == ".jpg":  # check if it's a jpg
                self.selectedFiles.append(file)
                self.files_selected+=1
            else: # file is not jpg, then skip
                self.files_skipped+=1
                pass
