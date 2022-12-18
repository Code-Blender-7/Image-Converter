import os
import sys
import PIL

from PIL import Image

TargetFileType = ".jpg"


class model():

    def __init__(self):
        self.targetDir = None
        self.files_scanned = 0
        self.files_selected = 0
        self.files_skipped = 0
        self.files_converted = 0
        self.selectedFiles = []

        
            
    def clear(self):
        """
        Reset all the values of the object attributes
        """
        self.files_scanned, self.files_selected, self.files_skipped, self.selectedFiles = 0,0,0,[]

            
    def validate_dir(self, directory):
        if os.path.isdir(directory): return True
        else: raise Exception


    def getTargetDir(self, textMsg):
        """
        get the target directory.
        try/except for special EOFError Handling.
        Doesn't end until a correct directory is given.
        """
        while True:
            try:
                directoryChoice = input(textMsg)
                if self.validate_dir(directoryChoice) == True: 
                    self.targetDir = directoryChoice
                break
                
            except Exception as err:
                print("Directory invalid or False Input. Please Try again.")
                continue


    def updateDir(self): 
        self.clear()

        for file in os.listdir(self.targetDir):
            self.files_scanned+=1
            if os.path.splitext(file)[1] == TargetFileType:  # check if it's a jpg
                self.selectedFiles.append(file)
                self.files_selected+=1
            else: # file is not jpg, then skip
                self.files_skipped+=1
                pass
        

    def saving_images(self, saving_dir=None):
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

    
    def createDir(self):
        choice = input("Create new Directory? [y/n]")
        if choice == "y":
            self.getTargetDir("Enter the directory you wish to create: ")
            try:
                os.mkdir(self.targetDir)
            except FileExistsError:
                print("Warning, This file already exists")
        elif choice == "n": return
    
    
    def customSavingDir(self):
        self.getTargetDir(f"Enter the directory to save the converted files: ")
        if self.validate_dir(self.targetDir) == False: 
            print("Error, this directory doesn't exist")
            self.createDir()
