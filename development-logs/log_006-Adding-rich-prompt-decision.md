# START

The rich prompt is a feature that comes with the rich library. Technically it is the alternative to the built-in input method of the python language. 

There had been a choice of conflict either to change all the inputs into rich.prompt where it feels like rich.prompt should be inside the view catagory. After the debates, I decided to plcae the rich.prompt inside the model instead of view. The reason is that the rich library has a built in rendered input method that doesn't need some custom designs like calling console from the rich library. That would either be a violation to the MVC. There is another method. That is to add the class of the rich.prompt to the model via the controller. That is quite crazy but if done, the MVC is not that much violated.


#### UPDATE

The rich.prompt will not be in the model nor view. The Confirm is instead to be used on the controller. It will inherit the class from view onto a variable. After that, the variable from view will be imported to the Controller.