"""
note. this is a stable version of the code. Please run it continuously and once you understood how it works, make sure to have a backup
"""


import os
import sys
import PIL
from PIL import Image
from rich.console import Console
from rich.progress import Progress
import time

selectedFiles = []
files_selected = 0
files_skipped = 0
files_detected = 0

console = Console()


def scan_dir(target_dir):
    """
    scan of the directory
    Note. call it once. otherwise it will keep adding/incrementing as times called.
    """
    # update values
    global files_skipped
    global files_selected
    global files_detected
    global selectedFiles

    for file in os.listdir(target_dir):
        files_detected+=1
        if os.path.splitext(file)[1] == ".jpg":  # check if it's a jpg
            selectedFiles.append(file)
            files_selected+=1
        else: # file is not jpg, then skip
            files_skipped+=1
            pass
        
    console.print(f"total skipped files: {files_skipped}")
    console.print(f"total detected files: {files_detected}")
    console.print(f"total selected files: {files_selected}")


def saving_images(file_list , saving_dir):
    """
    saves file image from a given directory.
    """
    with Progress(transient=True) as progress:
        task_1 = progress.add_task("[blue]Converting files...", total=len(file_list)) # total files are the selected files

        for file in file_list:
            img = Image.open(f"{target_dir}/{file}")
            img.save(f"{saving_dir}/{file}.png")
            progress.update(task_1, advance=1) # advance progress after 1 file is converted

    console.print(f"Files saved at [i][blue][blink2]{saving_dir}[/]")



def script_Runtime(target_dir):
    """
    code block for execueting user choice of the directory selection
    prints analytics of the selected target .directory
    """

    while True:
        userChoice = input("\nCreate a new directory? [y/n]: ")
        
        if userChoice.lower() == "n": # save all files on the target directory
            saving_images(selectedFiles, saving_dir=target_dir)
            break

        elif userChoice.lower() == "y": # save all files on a new given directory
            saving_dir = input("Enter new directory for saving files: ")
            os.makedirs(saving_dir)
            saving_images(selectedFiles, saving_dir)
            break

        else: # if the response is not expected, continue loop
            console.print(f"[red]Warning: Not a valid response[/]\n[red]Valid response either y or n. Got [/]{userChoice}\n[yellow]Try again[/]")


def main(target_dir):
    try: 
        scan_dir(target_dir) # running this causes the files to be updated
    except FileNotFoundError: 
        console.print("[red]Warning![/] No such file folder exists.")
        return True
    
    if len(selectedFiles) == 0: # if length of selected files is 0, continue loop.
        console.print("[red]Warning: No images found to convert to png[/]\n[yellow]Try Again.[/]")

    elif len(selectedFiles) > 0: # if length of selected files is not 0, break loop after saving
        console.print("[green]Images found")
        script_Runtime(target_dir)
        return False
    
try:
    while True:
        target_dir = input("Enter your directory here: ")
        if main(target_dir) == False: break # break loop if the function is completed. 
except KeyboardInterrupt:
    console.print("\n[blue]Program exiting now....[/]")
    sys.exit()