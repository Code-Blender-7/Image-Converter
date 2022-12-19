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
        if modelControl.file_placement_choice() == True: 
            modelControl.customSavingDir(self.renderer.insert_SavingDirMsg())
            
        else: return
    
    
    def runtime(self):
        while True:
            try:
                self.controlModelDir()
                if self.controlModelSavingImg() == False: continue
            except KeyboardInterrupt:
                print("Program quit")    

            finally: break
        
        
def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()
    
    
