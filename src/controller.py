from model import model

from view import render, CustomException
from view import text_art
from view import console

from support import prog_description

from rich.prompt import Confirm
from rich.console import Console

import os

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
                choice = Confirm.ask("\nSave files in another directory? [y]\nSave files in current Directory [n]")
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
        try:
            with console.screen():
                modelControl.saving_images()
        except KeyboardInterrupt: 
            raise CustomException(KeyboardInterrupt, 105)

        
    def runtime(self):
        while True:
            try:
                with console.screen():
                    text_art()
                    self.controlModelDir()
                    
                    if modelControl.files_selected > 0:
                        if self.controlModelSavingImg() == False: continue
                        self.display_ConvertProcess()
                        
                
            except KeyboardInterrupt:
                CustomException(KeyboardInterrupt, 101)
            
            except EOFError as error:
                sys.exit()

            break

    
def init():
    # prog_description()
    
    Controller()
        
if __name__ == "__main__":
    init()
    
    
