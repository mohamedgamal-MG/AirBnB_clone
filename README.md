irBnB Clone Project
Welcome to the AirBnB clone project! This is the first step towards building your first full web application: the AirBnB clone. The first step is to write a command interpreter to manage your AirBnB objects.

Project Tasks
Each task is linked and will help you to:

Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of your future instances.
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
Create the first abstracted storage engine of the project: File storage.
Create all unittests to validate all our classes and storage engine.
Command Interpreter
What is a command interpreter? Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (e.g. a new User or a new Place).
Retrieve an object from a file, a database, etc.
Do operations on objects (count, compute stats, etc.).
Update attributes of an object.
Destroy an object.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
