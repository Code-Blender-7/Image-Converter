import os
import sys
import PIL

from PIL import Image

TargetFileType = ".jpg"



class model():
    running = True
    defaultTargetDir = None
    def __init__(self):
        self.targetDir = ""
        self.files_scanned = 0
        self.files_selected = 0
        self.files_skipped = 0
        self.files_converted = 0
        self.selectedFiles = []
        self.listFiles = []
            
    def clear(self):
        self.files_scanned, self.files_selected, self.files_skipped, self.selectedFiles, self.listFiles = 0,0,0,[],[]
            
        

    def getTargetDir(self):
        """
        get the target directory. mutates two variables
        """
        self.clear()
        try:
            self.targetDir = input("Directory: ")
            model.defaultTargetDir = self.targetDir
            self.listFiles = os.listdir(self.targetDir)
        except Exception as error:
            print("Something went wrong", error)
            model.running = False
        return model.running
    
    

    def updateDir(self): 
        self.getTargetDir()
        for file in self.listFiles:
            self.files_scanned+=1
            if os.path.splitext(file)[1] == TargetFileType:  # check if it's a jpg
                self.selectedFiles.append(file)
                self.files_selected+=1
            else: # file is not jpg, then skip
                self.files_skipped+=1
                pass
        


    
    # Create a function that has a default arg of none 
    # it will be used to save the images based in the directory

    
    def saving_images(self, saving_dir=defaultTargetDir):
        """
        saves file image from a given directory.
        params: list, str
        """
        try:
            for file in self.selectedFiles:
                img = Image.open(f"{self.targetDir}/{file}")
                img.save(f"{saving_dir}/{file}.png")
                self.files_converted+=1
                print(file)    
                
            print(f"Total files converted (JPG => PNG) : {self.files_converted}\nFiles saved at [i][blue][blink2]{saving_dir}[/]")
        except KeyboardInterrupt:
            print("\n[red]Warn[/]. Program force-exit over converting process. Chances of corrupt-files is possible.")

        
