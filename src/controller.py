from model import model
from view import render, ExceptionHandler
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
        
        if modelControl.files_selected > 0: self.renderer.render_info()
        else:
            self.renderer.render_NO_FILES()
            return False
        

    def controlModelSavingImg(self):
        choice = modelControl.file_placement_choice()
        if choice == "y": 
            modelControl.customSavingDir(self.renderer.insert_SavingDirMsg())
        elif choice == "n": print("SAVING_IMAGE HERE")
         
        else:
            print(f"Error. {choice} is not a valid input")
            return False
    
    
    def runtime(self):
        while True:
            try:
                if self.controlModelDir() == False: continue
                if self.controlModelSavingImg() == False: continue
            except KeyboardInterrupt:
                ExceptionHandler("KeyboardInterrupt", 101)
                print("Program quit")
                modelControl.running = True    

            if modelControl.running == False: continue
            break
        
        
def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
