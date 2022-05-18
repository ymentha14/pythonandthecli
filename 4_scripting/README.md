# 4. Packaging your project 

The goal of this section will be to give you a way to write your code in scripts and to import it in other scripts and/or in notebooks.


## Solution 1: importing a local module
Your python interpreter will look for importable modules in the current directory, i.e. where you execute `python3` (among other, cf next solution). 
This can be useful for quick testing but does not scale at all for a whole project.

Still we want to test it: navigate to  `path/to/5_scripting/local_file_solution/`

and execute

        python3
        >> from module_bfh import say_hello
        >> say_hello()

Youpi, it works! Now go to any other directory (the parent one for instance)

        cd ..
        python3
        >> from module_bfh import say_hello
        #Traceback (most recent call last):
        #  File "<stdin>", line 1, in <module>
        #ModuleNotFoundError: No module named 'module_bfh'

As we saw, the installation was specific to this directory


## Solution 2: using PYTHONPATH

The environment variable `PYTHONPATH` must consists of a list of absolute paths separated by semicolon (`:`): the python interpreter will look in each of these directories for packages to import.

Let's take a look at the actual state of the pythonpath

        echo $PYTHONPATH
        # ""

In the previous example, we could not import our function from `path/to/5_scripting/local_file_solution/`

but if we run

        export PYTHONPATH=$PYTHONPATH:$(pwd)/local_file_solution

.. take a look at the state of the pythonpath


        echo $PYTHONPATH
        # /path/to/5_scripting/local_file_solution

.. and retry to import our package it should work

        python3
        >> from module_bfh import say_hello
        >> say_hello()

However, this solution requires you to export this environment variable each time and is therefore error-prone/ slow.

## Solution 3 packaging your project using setuptools 🚀

The 3rd solution consists in packaging your project using `setuptools`: this will lets you import your own code as easily as you import numpy or pandas :)

We are now facing a version of the code that is packaged: however this package is not installed yet.

### Files structure
Let's take a look at the structure of the project


        tree .
        .
        ├── commands.sh # The file you are currently reading
        ├── notebooks
        │   └── nb_v3.ipynb # The 3rd version of our iris notebook
        ├── requirements.txt # A file containing the dependencies of the project
        ├── setup.cfg # Allows to install src as a package
        ├── setup.py # Needs to be here next to setup.cfg but no need to understand it, just copy paste
        └── src
            ├── load.py # functions to load the data
            ├── transform.py # functions that transform the data
            └── visualization.py # functions to visualize the data

### Setup files
As the `setup.cfg` does not tolerate comments, we go through the structure of the file here:

`setup.cfg`

      [metadata]
      name = iris_bfh # the package name as you need to handle it with pip (typically to uninstall)
      [options]
      packages = src # the name of our package as we should import it
      package_dir =
        =. # where to look for the package: in our case, in the same directory as setup.cfg

### Installing the package
We will now see how to install our own code as a package:

jupyter lab

And try to run the code in `notebooks/nb_v3.ipynb`

      >> import src
      ModuleNotFoundError: No module named 'src'

There is an error as we did not install our package!

in `path/to/5_scripting/packaging_solution/`:

      python3 -m pip install .

You can now restart your jupyter kernel and retry. 

        >> import src

Success! (hopefully)
If you installed the kernel associated to this python interpreter, you should also be able to import `src` in a jupyter notebook

### Changing the code live in a notebook
There is still a problem: let's try to modify something in one of the functions in the `src` directory (_by adding a print statement for instance_) and call the function in a python shell

       (.. add a print statement in src/load.py)
       python3
       >> from src.load import load_iris_df

The change takes no effect!

To fix that we need to uninstall the local package

       python3 -m pip uninstall iris_bfh

And reinstall it __using the -e (editable) flag__

       python3 -m pip install -e .

This will create a few directories (build, wheel, egg) that you can ignore untill the end of the project. (If you happen to remove them, just repeat the last command we saw)

A quick python3 shell will show that our local package was successfully installed

       python3
       >> import src 

And we can now change code in the scripts for it to take effect immediately.

Note: if you change the code __while the python shell/jupyter notebook is running__ the change will not take effect until you restart it. If you want real _live_ updates, add the following lines at the top of your notebook:

        %load_ext autoreload
        %autoreload 2

Finally, you can install all your required package by running

        python3 -m pip install -r requirements.txt

Note that thanks to packaging, git is able to make the difference way more easily

        git diff src/load.py
## Bonus
If requirements.txt has the following structure

        # requirements.txt
        ######################
        package1
        package2
        packageN
        #####################

then running `python3 -m pip install -r requirements.txt` is equivalent to run:

        python3 -m pip install package1
        python3 -m pip install package2
        python3 -m pip install packageN

This is why we see the line

        -e .

at the top of requirements.txt :)

And how did we know which version to put in `requirements.txt`? If we want to check the version of our packages to make the code reproducible 

        python3 -m pip freeze

That's it! Good luck, and happy packaging :)

