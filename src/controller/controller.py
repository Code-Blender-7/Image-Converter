

import sys 
import os 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from model.model import model
from view.view import render, CustomException
from view.view import console, confirm, progress

from parseSupport import prog_description

modelControl = model()


class Controller():
    def __init__(self):
        self.renderer = render(modelControl)
        self.runtime()


    def render_savingfiles(self, savingDir):
        modelControl.saving_images(savingDir)
    

    def controlModelDir(self):
        while True:
            try:            
                modelControl.getTargetDir(self.renderer.enter_TargetDirMsg(), self.renderer.error_DirMsg())
                modelControl.updateDir()
                
                if modelControl.files_selected > 0: 
                    self.renderer.render_info()
                    break
                
                elif modelControl.files_selected == 0:
                    self.renderer.render_NO_FILES()
                    continue
                
            except EOFError:
                CustomException(EOFError)
                continue
    
    
    def controlModelSavingImg(self):
        """
        Summary:
        ==========
        Confirmation of the File Placement. Choice based.
        If Choice = "y": content to be saved inside another folder
        if Choice = "n": content to be saved inside the folder where the converting takes place
        
        """
        while True:
            try:
                choice = confirm.ask("\nSave files in another directory? [y]\nSave files in current Directory [n]")
                if choice: # choice = "y"
                    modelControl.customSavingDir(self.renderer.insert_SavingDirMsg())
                else: # choice = "n"
                    modelControl.currentSavingDir()
                
            except EOFError: 
                CustomException(EOFError)
                continue
            
            break
            
        
    # work on this # 
    def display_ConvertProcess(self):
        """
        Summary:
        ==========
        Function to handle the alternate screen for the converting process and to handle the display of the converting progress itself
        
        
        Raises:
        ==========
            CustomException: Custom Exception Handling Control
        
        """
        try:
            with console.screen():
                modelControl.saving_images(progress)
                
   
        except KeyboardInterrupt: 
            CustomException(KeyboardInterrupt, 105)

        
    def runtime(self):
        """
        Summary:
        ==========
        Main While Loop for the project. Calls function based on their actions serially.
        NOTE. Don't change the while loop unless you want to add a new feature to the code.
        
        """
        while True:
            try:
                with console.screen(hide_cursor=False):
                    self.renderer.text_art()
                    self.controlModelDir()
                    
                    if modelControl.files_selected > 0:
                        if self.controlModelSavingImg() == False: continue
                        self.display_ConvertProcess()
                
                self.renderer.convertCompleteResults()
                        
                
            except KeyboardInterrupt:
                CustomException(KeyboardInterrupt, 101)
                
            break

    
def init():
    prog_description()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
