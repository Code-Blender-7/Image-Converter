__PLEASE BE AWARE THAT THIS LOG COULD BE SOON CHANGED OR DEPRACICATED AS THE CODE OF THE ACTUAL PROJECT RAPIDLY BEING MODIFIED.__

# START

### Code Structure

The program takes a file directory and probes into it. After that, the results of the probe are separated into 3 catagories.

1. Files Scanned
2. Files Selected
3. Files Skipped

Of course, if a file is selected then it should be converted immediately. However if I did something like that, the structure of the code would be so messed up that future development would be harder.

Because of that, the probe selectes the selected files and then it stores them onto an array. That array is then passed to the saving image function where the images are read along with their file directory and after that, the pillow library selects the files, opens them and save them as a new format.

