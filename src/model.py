import os
import sys
import PIL

from PIL import Image
from helper import TargetFileType, SelectFileType

SelectFileType = ".jpg"
TargetFileType = ".png"

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
            # try:
            #     directoryChoice = input(textMsg)
            #     if directoryChoice == "": raise Exception("Value empty")
            #     elif self.validate_dir(directoryChoice) == True: 
            #         self.targetDir = directoryChoice
            #         break
            #     else: raise Exception
            
            # except Exception:
            #     print(errorMsg)
            #     continue
            

            directoryChoice = input(textMsg)
            if self.validate_dir(directoryChoice) == True: 
                self.targetDir = directoryChoice
                break
            else: 
                print(errorMsg)
                raise Exception
        
        

        
            
    
    def getSavingDir(self, textMsg, errorMsg):
        try:
            directoryChoice = input(textMsg)
            self.saving_images = directoryChoice
                
        except EOFError:
            print(errorMsg)
            
            
    def updateDir(self): 
        self.clear()

        for file in os.listdir(self.targetDir):
            self.files_scanned+=1
            if os.path.splitext(file)[1] == SelectFileType:  # check if it's a jpg
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
                img.save(f"{saving_dir}/{file}.{TargetFileType}")
                self.files_converted+=1
                print(file)    
                
            print(f"Total files converted (JPG => PNG) : {self.files_converted}\nFiles saved at [i][blue][blink2]{saving_dir}[/]")
        except KeyboardInterrupt:
            print("\n[red]Warn[/]. Program force-exit over converting process. Chances of corrupt-files is possible.")

    
    def file_placement_choice(self):
        if self.files_selected > 0:
            
            choice = input("\nSave files in another directory? [y]\nSave files in current Directory [n]\n: ")
            return choice
        else: return 
        
        
    def createDir(self, savingUserDir):
        while True:
            choice = input(f"Do you wish to create this directory?\nCreate Directory: {savingUserDir} \n[y/n]: ")
    
            if choice == "y":
                os.mkdir(savingUserDir)
                print("CUSTOM SAVING DIR HERE with PREDEFINIED DIRECTORY")
            
            elif choice == "n":
            
                try:
                    customDir = input("Enter the directory path you want to create: ")
                    if self.validate_dir(customDir) == True:
                        os.mkdir(customDir) 
                        print("CUSTOM SAVING DIR HERE with USER-DEFINIED DIRECTORY")

                    
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
