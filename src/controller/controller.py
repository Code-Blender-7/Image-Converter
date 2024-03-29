

import sys 
import os 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from model.model import model
from view.view import render, CustomException
from view.view import console, confirm, progress

import parseSupport
from markup import readme

modelControl = model()


class Controller():
    def __init__(self):
        self.renderer = render(modelControl)

    def render_savingfiles(self, savingDir):
        modelControl.saving_images(savingDir)

    def controlModelDir(self):
        while True:
            try:            
                modelControl.getTargetDir(self.renderer.enter_TargetDirMsg(), self.renderer.errorMessage())
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
                choice = self.renderer.filePlacementChoiceDisplay()
                if choice: # choice = "y"
                    modelControl.customSavingDir(self.renderer.insert_SavingDirMsg(), self.renderer.errorMessage())
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

if __name__ == "__main__":

    if parseSupport.args.readme:
        readme()
    elif parseSupport.args.start:
        Controller().runtime()
    else: parseSupport.parser.print_help() # display help if none of the quota matches

