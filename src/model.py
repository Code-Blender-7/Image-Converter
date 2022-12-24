import os
import sys
import PIL

from PIL import Image
from helper import _targetFileType, _selectFileType


class model():

    running = True
    
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
        Reset all the values of the object attributes
        """
        self.files_scanned, self.files_selected, self.files_skipped, self.selectedFiles = 0,0,0,[]

            
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
                raise Exception        
            
            
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
        

    def saving_images(self, saving_dir=None):
        """
        Summary:
        ==========
        Used for saving directory
        
        Args:
        ==========
            saving_dir (str/filePath, optional): Target File location. Defaults to None.
        
        """
        try:
            for file in self.selectedFiles:
                img = Image.open(f"{self.targetDir}/{file}")
                img.save(f"{saving_dir}/{file}.{_targetFileType}")
                self.files_converted+=1
                print(file)    
                
            print(f"Total files converted (JPG => PNG) : {self.files_converted}\nFiles saved at [i][blue][blink2]{saving_dir}[/]")
            
        except KeyboardInterrupt:
            print("\n[red]Warn[/]. Program force-exit over converting process. Chances of corrupt-files is possible.")

    
    
    def createDir(self, savingUserDir):
        while True:
            choice = input(f"Do you wish to create this directory?\nCreate Directory: {savingUserDir} \n[y/n]: ")
    
            if choice == "y":
                os.mkdir(savingUserDir)
                self.saving_images(savingUserDir)
            
            elif choice == "n":
            
                try:
                    customDir = input("Enter the directory path you want to create: ")
                    if self.validate_dir(customDir) == True:
                        os.mkdir(customDir) 
                        self.saving_images(customDir)

                    
                except FileExistsError:
                    print("Warning, This file already exists")
                    continue

            break            


    def customSavingDir(self, textMsg):
        directoryChoice = input(textMsg)
        
        # if directory doesn't exist, create new directory
        if self.validate_dir(directoryChoice) == False: 
            print("Error, this directory doesn't exist")
            self.createDir(directoryChoice)
            
        # work on this #
        # if user input is same from the directory of the converting folder, return to file placement choice
        elif self.targetDir == directoryChoice:
            print("Your new directory is the same from the folder you are converting")
            model.running = False
        
        else:
            print("PRE-EXISTING DIRECTORY SAVING IMAGE HERE!")
