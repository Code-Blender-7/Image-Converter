import argparse

def prog_description():
    parser = argparse.ArgumentParser(
        prog='controller.py')
    
    parser.add_argument("-r", "--readme",  help="Displays the markup file",
                        action="store_true")

    args = parser.parse_args()
    
prog_description()

# WORK IN PROGRESS #
# to enable, uncomment function in controller.py #