# 1. Virtual environments

## Installing the virtual environment 
Check which python is activated: the system one
We should never install any package on this interpreter as it might break basic computer functionalities

        which python3 
        # -> /bin/python3
        # or -> /usr/bin/python3

We therefore create a new virtual environment using the venv package (it is a python package! check out in a python console, you can import it)

        python3 -m venv bfh_env 

(optional) Check out the structure of the newly created directory

        tree -L 5 bfh_env

Anywhere you see a `bin` directory, you will find executable files, that is, files you can execute in the console as programs

We will now activate this environment

        source bfh_env/bin/activate

and make sure we have indeed access to the right python interpreter

        which python3 
        # -> /home/path/to/your/bfh_env/bin/python3

This refers to the python3 executable in the virtual environment: as long as the virtual env is active, it is this python we will refere to when typing `python3` in the console.

## Installing python package in the virtual environment 

Now try to import pandas in a python console: pandas is not installed

          python3
          >> import pandas
          # -> ModuleNotFound: pandas

We therefore want to install it. In order to make sure we install it in the current virtual environment and not in the system python, we use the `python3 -m ` option to make sure that pip will install the package for the right interpreter.

          python3 -m pip install pandas

Rerry to import pandas: 

          python3
          >> import pandas 

Cool! pandas has successfully been installed  :)

## Setting up jupyter kernel 

In order to have jupyter notebooks running, install the jupyter lab package

          python3 -m pip install jupyterlab

(Jupyter lab is just like jupyter notebooks, but offers more features generally speaking)
Run a jupyter lab instance

          jupyter lab

From there you can start a notebook and start coding!
 
in a notebook:

         >>: import pandas
From now on you can leave this console running and start a new console. Once again, make sure to activate the virtual environment in order to operate with the right interpreter:

         source path/to/2_virtual_envs/bfh_env/bin/activate
         python3 -m ipykernel install --user --name my_first_bfh_kernel

The last option created a jupyter kernel: basically, a kernel is a way to select the right interpreter for the notebook from jupyterlab without having to worry about which virtualenv was active to start it. lick on the top right option of jupyter: this open a popup window "Select kernel". `my_first_bfh_kernel` should appear. Select it and retry importing pandas. Success! (hopefully) From now on, every package we will install on this interpreter will be available on this jupyter kernel :)

To illustrate that, let's create a second virtual environment, for a second fictive project, for which we don't need the `pandas` library but the `wasabi` one: here is a one-liner that execute all the commands we saw at once (creating a second virtual env, activating it, installing `wasabi` and `jupyterlab` and installing the jupyter kernel.

          python3 -m venv second_env && \
          source second_env/bin/activate && \
          python3 -m pip install wasabi jupyterlab && \
          python3 -m ipykernel install --user --name second_env_kernel

Although we did not start a second instance of jupyter, (jupyter is still executed from our first virtual env) we can refresh the page, go to 'Select kernel' and see our 'second_env_kernel' that was successfully installed! Try to create a new notebook selecting this kernel and execute

          >> import wasabi
 
On the other hand you cannot import pandas, as it was installed on the other env
          
          >> import pandas
          ModuleNotFoundError: pandas

Additionally, you can execute CLI commands in any notebook by preceding them by a `!`: try running

          !which python3

This should point to the second virtual env python3 executable. That's it!

          
