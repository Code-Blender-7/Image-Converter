from model import model
from view import render
from view import text_art


running = True
modelControl = model()


class Controller():
    def __init__(self):
        self.userTargetDirectory = self.getTargetDirectory()
        self.renderer = render(modelControl)
        self.main_loop()
    

    def getTargetDirectory(self):
        try:
            userTargetDirectory = input("Directory: ")
        except EOFError:
            print("Warning, Please insert a valid directory")
        return userTargetDirectory    
            
    
    def file_placement_choice(self):
        choice = input("Create new Directory? [y/n]")
        if (choice == "y"):
            print("Positive")
        elif (choice == "n"): 
            print("Negative")
        else:
            return False
                

    def main_loop(self):
        while running:
            modelControl.scan_dir(self.userTargetDirectory)
            self.renderer.render_info()
            if modelControl.files_selected == 0: break
            self.file_placement_choice() 
   

def init():
    text_art()
    Controller()
        
if __name__ == "__main__":
    init()