
# START

This is it. The implementation of the Model Controller View. Well, this was totally not necessary because it would just be another project dead in the waters after completion. However, I wanted to turn the architecture of this project ASAP as a future reference to write all my projects if possible to the MVC architecture.

First off, there is a backup main file that contents the stable version of the project. In case the convertion fails, the actual file stays intact.

Let's talk about the placement of the project parts.

### Creating Model, View, Controller

Controller must be the centerpiece of the project. This file will control the user interaction with the main project. 
Model wil be the placement to handle the logic bussiness logic of the project. That includes to display the results of the folder and to save the files.
View is the rendering file for the project. That includes the display over the terminal for the user over the results.


There are a couple of things that I should specify. 
1. The Controller can only have 1 while loop. Model and View cannot have while loops
2. Attribute to classes is not granted unless one or more functions needs them.
3. Project is strictly MVC. Maintain the law.
4. In case of failure, delete all evidence and revert to backup.
5. The variables and others are declared and used in a desending order.