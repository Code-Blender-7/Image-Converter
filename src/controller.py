from model import model
from view import render
from view import text_art


modelControl = model()       
class Controller():
    def __init__(self):
        self.renderer = render(modelControl)
        self.main_loop()



    def file_placement_choice(self):
        choice = input("Save files in current directory? [y/n]: ")
        if (choice == "y"):
            print("Negative")
        elif (choice == "n"): 
            modelControl.customSavingDir()
        else:
            print("Invalid Command")
            return False
                

    def render_savingfiles(self, savingDir):
        modelControl.saving_images(savingDir)
        
    
    
        
        
        

    def main_loop(self):
        while modelControl.running:
            if modelControl.updateDir() == False: continue
            if modelControl.files_selected == 0: break
            self.renderer.render_info()
            if self.file_placement_choice() == False: break 

   

def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
