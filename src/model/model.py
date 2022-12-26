import os
import sys
import PIL

from PIL import Image
from helper import _targetFileType, _selectFileType


class model():
    
    def __init__(self):
        self.targetDir = None
        self.savingDir = None
        self.files_scanned = 0
        self.files_selected = 0
        self.files_skipped = 0
        self.files_converted = 0
        self.selectedFiles = []

        
            
    def clear(self):
        """
        Summary:
        ==========
        Resetting the values of the class variables 
           
        """
        self.files_scanned, self.files_selected, self.files_skipped, self.selectedFiles = 0,0,0,[]
        self.savingDir = None

            
    def validate_dir(self, directory):
        """
        Summary:
        ==========
        directory validator. Uses OS Lib to check if the directory exists or now
        
        Args:
        ==========
            directory (str/int): File directory location on the system
        
        Returns:
        ==========
            bool: if True then it exists,  If False, It doesn't
        
        """
        if os.path.isdir(directory): return True
        elif not os.path.isdir(directory): return False


    def getTargetDir(self, textMsg, errorMsg):
        """
        get the target directory.
        updates the targetDir of the class
        try/except for special EOFError Handling.
        
        params 1: textMsg: str [directory location], 
        params 2: errorMsg:str [error message]
        """
        while True:
 
            directoryChoice = input(textMsg)
            if self.validate_dir(directoryChoice) == True: 
                self.targetDir = directoryChoice
                break
            else: 
                print(errorMsg)
                continue


            
    def updateDir(self): 
        self.clear()

        for file in os.listdir(self.targetDir):
            self.files_scanned+=1
            if os.path.splitext(file)[1] == _selectFileType:  # check if it's a jpg
                self.selectedFiles.append(file)
                self.files_selected+=1
            else: # file is not jpg, then skip
                self.files_skipped+=1
                pass
        

    def saving_images(self, progress):
        """
        Summary:
        ==========
        Used for saving directory
        Requires Target directory and Selected Files list
        Externally needs type of files to convert from and to
        
        Args:
        ==========
            saving_dir (str/filePath): Saving folder location
        
        """
        
        with progress:
            task_1 = progress.add_task("Working..", total=len(self.selectedFiles)) # total files are the selected files

            for file in self.selectedFiles:
                img = Image.open(f"{self.targetDir}/{file}")
                img.save(f"{self.savingDir}/{file}{_targetFileType}")
                progress.update(task_1, advance=1) # advance progress after 1 file is converted
                self.files_converted+=1
                print(file)
  
  
  
    def createDir(self, savingUserDir):
        while True:
            choice = input(f"Do you wish to create this directory?\nCreate Directory: {savingUserDir} \n[y/n]: ")
    
            if choice == "y":
                os.mkdir(savingUserDir)
                self.savingDir = savingUserDir
            
            elif choice == "n": 
                return

            else: 
                print("Invalid Command")
                continue
            
            break            


    def currentSavingDir(self):
        """
        Summary:
        ==========
        used to save files in the current directory
        created to make sure all the savings operations are triggered inside the model
        """
        self.savingDir = self.targetDir


    def customSavingDir(self, textMsg):
        """
        Summary:
        ==========
        used to save files in another folder if the user doesn't chose to save files in current directory
        
        Args:
        ==========
            textMsg (str): Placeholder text for Input class. Gets from Controller 
        
        """
        while True:
            newSavingDir = input(textMsg)
            
            # if directory doesn't exist, create new directory
            if self.validate_dir(newSavingDir) == False: 
                print("Error, this directory doesn't exist")
                self.createDir(newSavingDir)
                
                
            # if user input is same from the directory of the converting folder, return to file placement choice
            elif self.targetDir == newSavingDir:
                print("Your new directory is the same from the folder you are converting")
                continue
            
            else:
            # if the saving dir exists on the machine, save the files there
                self.savingDir = newSavingDir
            
            break
