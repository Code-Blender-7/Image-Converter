import argparse

def prog_description():
    parser = argparse.ArgumentParser(
        prog='controller.py')
    
    parser.add_argument("-r", "--readme",  help="Displays readme markdown file",
                        action="store_true")

    args = parser.parse_args()
    
prog_description()