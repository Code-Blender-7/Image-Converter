from model import model
from view import render
from view import text_art


modelControl = model()
class Controller():
    def __init__(self):
        self.renderer = render(modelControl)
        # self.main_loop()
        self.runtime()


    def render_savingfiles(self, savingDir):
        modelControl.saving_images(savingDir)
    

    def controlModelDir(self):
        modelControl.getTargetDir(self.renderer.enter_TargetDirMsg(), self.renderer.error_DirMsg())
        modelControl.updateDir()
        self.renderer.render_info() if modelControl.files_selected > 0 else self.renderer.render_NO_FILES()


    def controlModelSavingImg(self):
        choice = modelControl.file_placement_choice()
        if choice == "y": 
            modelControl.customSavingDir(self.renderer.insert_SavingDirMsg())
            
        else:
            print(f"Error. {choice} is not a valid input")
            modelControl.running = False
    
    
    def runtime(self):
        while True:
            try:
                self.controlModelDir()
                if self.controlModelSavingImg() == False: continue
            except KeyboardInterrupt:
                print("Program quit")
                modelControl.running = True    

            if modelControl.running == False: continue
            break
        
        
def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
