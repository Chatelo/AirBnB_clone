# AirBnB Clone Project
# AirBnB clone - The console


This is the first piece of tihe AirBnB project which is among the major projects Alx students are tasked. It sheds light on file serialization, objects and creation of a file storage.
It is command line interface from which you can create and modify files in storage before you can build up on the rest of your AirBnB application.
# Base Model
Base Model is the project’s parent class that will handle initialization, serialization and deserialization of future instances.
All other clases will inherit from the base class.
# Create other classes
Class User, State, City, Place among other classes created will all inherit from the parent class Base Model.

# Command-line interpreter
Program that provides a text based interface for interacting with an operating system or executing commands.
# Starting the command interpreter
1. Clone the AirBnB_clone repository on your local machine.
2. Next navigate to the project directory.
3. Run the command interpreter script './console.py'.
Once the interpeter is running, you can enter commands to manage the AirBnB project.
****Command format****
(command) (class) (action) (arguments)

****eg****
Destroying a City object -> (hbnb) destroy City 9876-5432-1098
Listing all objects of a specific class -> (hbnb) all User

*********Command list*********
-   `create`: Creates a new object of the specified class.
-   `show`: Displays the string representation of an object.
-   `destroy`: Deletes an object from the system.
-   `all`: Lists all objects of a specific class or all objects if no class is specified.
-   `update`: Updates the attributes of an object.

# Uses of the command interpreter
A command interpreter in the context of the AirBnB clone project will provide a way for users to manage the AirBnB prioject.
1. Create new objects -> User, Place etc
2. Retrieving objects from storage.
3. Performing operations on objects -> eg Counting, computing statistics etc.
4. Updating object attributes.
5. Destoying objects.

# Examples 
Bash(Bourne Again Shell): Default command-line shell in unix ,linux and macOS.
Windows Command Prompt(cmd.exe)
PowerShell: commmand-line developed by windows for windows, macOS and linux.
Zsh(ZShell)
Fish(Friendly Interactive SHell)
Csh(CShell)

# Python modules
Cmd module
‘cmd.Cmd’ class provides a convinient framework for building interactive command-line programs in Python.
sys module
Builtin python module that grants access to various system-specific parameters and functions.
# Unit tests
To ensure the correctness of your implementation, it is important to create unit tests for all classes and the storage engine. Unit tests will validate the behavior and functionality of your code, helping to identify and fix any issues that may arise.
# Storage Engine
Additionally, you will need to create a storage engine, starting with a file storage system. This storage engine will handle the reading and writing of objects to files, providing the functionality required for object persistence.
You will also need to implement a flow of serialization/deserialization, which involves converting instances of objects to dictionaries, JSON strings, and storing them in files.


# Authors
This project is a collaborative effort. The following individuals have contributed to the repository:
Benard Ronoh  <biikate48@gmail.com>
wambui-mungai <wambuim220@gmail.com>

### Branches and Pull Requests

To facilitate team collaboration and organization, we will be using branches and pull requests on GitHub.
