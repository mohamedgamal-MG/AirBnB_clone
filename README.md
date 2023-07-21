![logo](web_static/images/logo.png)
# Project Description

This is a command-line interface program that provides a command interpreter for an AirBnB clone project. The program allows users to create, manipulate, and delete different objects such as users, states, cities, places, and reviews. The program uses Python3 and is compatible with both the interactive and non-interactive modes.

# Command Interpreter Description

The command interpreter is a Python3 program that provides a command-line interface for the user. It uses the `cmd` module to create a command interpreter that parses user input and executes the appropriate command. The program includes a set of pre-defined commands that can be used to create, manipulate, and delete different objects in the AirBnB clone project.

## How to Start the Command Interpreter

To start the command interpreter, run the following command in your terminal:

```bash
./console.py
```

This will start the program in interactive mode and display the command prompt `(hbnb)`.

## How to Use the Command Interpreter

The command interpreter provides a set of pre-defined commands that can be used to create, manipulate, and delete different objects. The following is a list of the available commands:

- `create`: creates a new object
- `show`: displays the details of an object
- `destroy`: deletes an object
- `all`: displays all objects
- `update`: updates the properties of an object
- `quit`: exits the command interpreter

To use any of these commands, simply type the command name followed by the appropriate arguments. For example, to create a new user, type the following command:

```
(hbnb) create User
```

This will create a new user object and return its ID. To display the details of the user, use the following command:

```
(hbnb) show User <user_id>
```

Where `<user_id>` is the ID of the user object. Similarly, you can use the `update` command to update the properties of an object, and the `destroy` command to delete an object.

## Examples

Here are some examples of how to use the command interpreter:

1. Create a new user:

```
(hbnb) create User
```

2. Display the details of the user:

```
(hbnb) show User 1234-5678-9012
```

3. Update the name of the user:

```
(hbnb) update User 1234-5678-9012 name "John Doe"
```

4. Delete the user:

```
(hbnb) destroy User 1234-5678-9012
```

5. Display all users:

```
(hbnb) all User
```

These are just a few examples of the many commands that are available in the command interpreter. For more information on how to use the program, refer to the help command:

```
(hbnb) help
```

This will display a list of all available commands and provide more information on how to use them.
