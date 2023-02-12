
### Table of Contents
1. [Demo](#demo)
2. [Project-Introduction](#project-introduction)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Note](#note)
6. [Credits](#credits)

## Demo

![](https://github.com/Code-Blender-7/assets/blob/main/Image-Converter/demo.gif)

# Project-Introduction

Image Converter is a python image conversion tool that changes jpg images to png formats. This is an utility tool that works in bulk by selecting a folder and converting all the JPG images to PNG format.

Image Converter is based on python and it is recently upgraded with the rich-cli library to provide beautiful syntax output to the user.

## Installation

Follow this steps to install the program over your computer.
1. Install the Python programming language over your machine from the official website [here](https://www.python.org/).
    _For those who are new to this, be sure to check __"Add to PATH"__ during Installation process._

    If you have successfully installed it, confirm it via your command prompt and typing this,
    ```
    python --version
    ```
2. Clone this repo via your package manager.
    for git...
    ```
    git clone https://github.com/Code-Blender-7/Image-Converter
    ```
3. Install dependencies
    ```
    python install -r requirements.txt
    ```

After that, you are good to go!

## Usage
Open the program folder after navigating to the root folder where the project is located.

Run the program via your command prompt or any terminal you wish to use
```
$ cd src/controller
$ python controller.py
```
To execuete the program, go to ```root/src/controller/``` then,
```
python controller.py --start
```

## Note
Please run the code over the most modern terminals to ensure the program to use its full potential like Windows Terminal.

Also be aware that this project uses the Rich Lbrary which is CLI based. Changing the terminal sizes could bring unknown results. However, the script will work nevertheless.


## FAQ

1. Which format can this program script handle?
> .JPG

2. Which files would be changed?
> All the files that are .JPG in the directory where you gave the directory name.

3. Would my file be duplicated if I run this program twice in the same directory?
> No. If it was converted then it is simply rewritten. A new feature would be added to notify users of such rewritting.

4. Would my previous files be removed?
> No. But a feature would be ready for that. I will implement it when I have time.

5. I want to contribute to this project
> The issue is open and you can message me on my Twitter acc.

## Credits

Built with :heart: by [@Black_2_white](https://twitter.com/@Black_2_white).

