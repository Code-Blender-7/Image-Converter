from model import model

from view import render, CustomException
from view import text_art

from support import prog_description

from rich.prompt import Confirm
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
            modelControl.getTargetDir(self.renderer.enter_TargetDirMsg(), self.renderer.error_DirMsg())
            modelControl.updateDir()
            
            if modelControl.files_selected > 0: 
                self.renderer.render_info()
                break
            else:
                self.renderer.render_NO_FILES()
                continue
        
    
    def controlModelSavingImg(self):
        """
        Summary:
        ==========
        Confirmation of the File Placement. Choice based.
        If Choice = "y": content to be saved inside another folder
        if Choice = "n": content to be saved inside the folder where the converting takes place
        
        """
        choice = Confirm.ask("\nSave files in another directory? [y]\nSave files in current Directory [n]")
        if choice: 
            modelControl.customSavingDir(self.renderer.insert_SavingDirMsg())
        else: modelControl.currentSavingDir()
    
    
    
    def display_ConvertProcess(self):
        modelControl.saving_images(modelControl.savingDir)
        # self.renderer.renderConverting(modelControl.saving_images(modelControl.savingDir))

        
    def runtime(self):
        while True:
            try:
                self.controlModelDir()
                
                if modelControl.files_selected > 0:
                    self.controlModelSavingImg()
                    self.display_ConvertProcess()
                    
                break
                
            except Exception as err:
                if err != KeyboardInterrupt:
                    continue
                
            except KeyboardInterrupt:
                CustomException(KeyboardInterrupt, 101)
                
            break
        
        
def init():
    # prog_description()
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
