
# START

The project has incorporated nearly 45% of the original project's capability. However, there are other things to remember and that is that  the project is constantly changing its architecture over and over in aspects of how the code should be written.

As long as this issue comes up, the project is rolled back to 0% again.

For me, I recommend that the code itself should not be written all inside controller. Every core functionality is indeed handled by the controller but I recommend that controller should be more like a "assigner" than a "task handler". That means that the controller can only call over to the model.py as times needed. the code works as a decending order where the code is processed from one block to another. It also means that the code cannot have a single while loop. I tried to make it so but the code is too harder for me to process. For that reason, it is recommended to create while loops inside model.py and then call them all over the controller.py

