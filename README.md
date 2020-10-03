
model.py:


It consists of pure application logic, which interacts with the database. It includes all the information to represent data to the end-user.
here all the calculation logic is represented which is used when the user enters the no.s which are to be calculated


view.py

View represents the HTML files, which interact with the end-user. It represents the model’s data to the user.
it represents the user interface for the users for the input and getting the data for further calculations.



controller.py

It acts as an intermediary between view and model. It listens to the events triggered by the view and queries model for the same.
it helps the view and model for interacting as and when needed by the program according to the user input



main.py

it is the core part of the program which links all the M V C togethering resulting in a working calculator application it is responsible for creating
and calling of the objects
