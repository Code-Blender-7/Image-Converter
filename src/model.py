import os
import sys
import PIL

from PIL import Image

TargetFileType = ".jpg"


class model():
    running = True
    def __init__(self):
        self.targetDir = ""
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


    def getTargetDir(self, textMsg):
        """
        get the target directory. mutates two variables
        """
        try:
            self.targetDir = input(textMsg)
        except Exception as err:
            print(err)
            
        return model.running
    
    def validate_dir(self, directory):
        if os.path.isdir(directory):
            return True
        else:
            return False


    def updateDir(self): 
        self.clear()
        self.getTargetDir("Enter the directory you want to convert the files: ")
        if self.validate_dir(self.targetDir) == False: 
            print("Warning, directory not found")
            return False

        elif self.validate_dir(self.targetDir) == True:        
            for file in os.listdir(self.targetDir):
                self.files_scanned+=1
                if os.path.splitext(file)[1] == TargetFileType:  # check if it's a jpg
                    self.selectedFiles.append(file)
                    self.files_selected+=1
                else: # file is not jpg, then skip
                    self.files_skipped+=1
                    pass
            
        return model.running
        


    
    # Create a function that has a default arg of none 
    # it will be used to save the images based in the directory

    
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
