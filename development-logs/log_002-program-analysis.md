__PLEASE BE AWARE THAT THIS LOG COULD BE SOON CHANGED OR DEPRACICATED AS THE CODE OF THE ACTUAL PROJECT RAPIDLY BEING MODIFIED.__




THIS LOG IS ABOUT THE PROGRAM BEHAVIOR OF Image-Converter AND ITS CODE ANALYSIS.

# START

### What does the project do?

The project simply transforms the JPG to PNG format. That is it!

Well, the project "work" as a interface to convert the files. The majority of the credits goes to the Pillow library because that is what does the magic.


#### Explaining the process
The programs takes the value of "target directory". If the user doesn't give the directory, it would still ask for it. Taking the advantage of the simple try/exception concept of python; The project can have different KeyWord Exceptions at different stages of the Program.

The Project after getting the directory displays the result over the terminal to the user. That is enough to let the user be aware of the total files that could be converted if they require so.

Afterwards comes the real fun. The program would seek either the file should be saved over the current directory or the file should be saved over a new folder.

The inputs are over a Y/N sequence. There were suggestions of "a" as select all sequence but that is rejected for now.


One thing that you'll notice is the sudden change of the display like a new screen was created. Well, that is the power of the console.screen() This is all entirely rich functionality.

Afterwards, the project shows the names of the files that are being converted over the time. This is a cool feature of the program because it is so satisfying to watch the files be processed.

A live-progress is created showing the percentage of the completion. If the percentage is reached, the program will exit after that. In the end, it will display the location of the files where the converted images were saved.

