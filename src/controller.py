from model import model
from view import render
from view import text_art


modelControl = model()       
class Controller():
    def __init__(self):
        self.renderer = render(modelControl)
        self.main_loop()



    def file_placement_choice(self):
        choice = input("Create new Directory? [y/n]: ")
        if (choice == "y"):
            self.render_savingfiles(input("Enter the directory you want to save: "))
        elif (choice == "n"): 
            print("Negative")
        else:
            print("Invalid Command")
            return False
                

    def render_savingfiles(self, savingDir):
        modelControl.saving_images(savingDir)

    def main_loop(self):
        while modelControl.running:
            modelControl.updateDir()
            self.renderer.render_info()
            if modelControl.files_selected == 0: break
            if self.file_placement_choice() == False: break 
            break

   

def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
