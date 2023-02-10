import argparse

from markup import markup
import os
import sys


parser = argparse.ArgumentParser(
    prog=f'{os.path.basename(sys.argv[0])}',
    description="Image Converter converts all your JPG images to PNG in a single folder.",
    )

parser.add_argument("-r", "--readme",  help="Displays the markup file. STILL IN BUILT",
                    action="store_true")
parser.add_argument("--start", help="Activates the program", action="store_true")

args = parser.parse_args()

# WORK IN PROGRESS #
# to enable, uncomment function in controller.py #