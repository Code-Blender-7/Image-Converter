from model import model
from view import render
from view import text_art

renderer = render()

while True:
    text_art()
    userChoiceTargetDir = input("Input your target dir here")
    tester = model(userChoiceTargetDir)
    # renderModule = render(tester)
    renderer.render_info(obj=tester)
    
    