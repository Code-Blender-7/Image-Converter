from model import model
from view import render
from view import text_art


modelControl = model()       
class Controller():
    def __init__(self):
        self.renderer = render(modelControl)
        # self.main_loop()
        self.runtime()



    def file_placement_choice(self):
        
        choice = input("\nCreate new Directory to save files? [y]\nSave files in current Directory [n]\n: ")
        if (choice == "y"): return
        elif (choice == "n"): 
            modelControl.customSavingDir()
        else:
            print("Invalid Command")
            return False
                

    def render_savingfiles(self, savingDir):
        modelControl.saving_images(savingDir)
    
    
    # def main_loop(self):
    #     while modelControl.running | True:
    #         if modelControl.updateDir() == False: continue
    #         if modelControl.files_selected == 0: break
    #         self.renderer.render_info()
    #         if self.file_placement_choice() == False: continue 


    def controlModelDir(self):
        modelControl.getTargetDir("Enter the directory you want to convert the files: ")
        modelControl.updateDir()
        self.renderer.render_info() if modelControl.files_selected > 0 else self.renderer.render_NO_FILES()

    
    def runtime(self):
        self.controlModelDir()
        

def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
