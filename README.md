# Python Tutorial
This tutorial aims at introducing a few good practices when doing data analysis in python. It is by no mean an exhaustive resource, and google stays your best friend in most cases, but we will try to cover the basics that are not enough taught (in my opinion). Among them:

### General goals:
* Clarity
* Reproducibility
* Efficiency
* More fun :)

### Types of issues we'll try to solve:
* Unreproducible environment
* Bug with package installations
* Bug with notebook execution

NB: for the sections 2,3,4,5 please run `make create_env` at the level of the `Makefile` file to create the appropriate virtual environment (hint: if you understood section 1, take a look at the command that is present under `create_env` in the `Makefile`). All experiments in these sections are meant to be executed using the `main_env` virtual environment.

## Setup a proper IDE
Notebooks are a great tool to start developping as they provide the user with an *interactive* environment that allows to:

* Test functionalities on-the-fly
* Perform inline data visualization

However, this same interactivity feature make notebook relatively difficult to share across collaborators. Indeed, one needs to ensure that the notebook runs *sequentially* before sharing it with anyone, since the execution flow followed during development might not correspond to the sequential one.

Python scripts don't share this issue, as sequential execution is guaranteed.

In summary:

* Develop and test functions and modules in notebook
* Once they work properly, move them to a python script
* Import the refactored functionalities in the initial notebook
* The initial notebook should consist exclusively of calls to visualization functions

## List of Integrated Development Environments
* VScode
* Pycharm
* Atom
* Eclipse

## Virtual environments
### Conda or pip?
* Make sure to install the right package in the right tool!
* Use `which` and `python3 -m pip install ...`

