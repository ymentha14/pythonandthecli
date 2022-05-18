# 5. Debugging
In this version of the project, a bug was introduced (an out-of-range indexing error in `path/to/6_debugging/src_debug/load.py:load_iris_df (line 14)` We will see three different methods to debug it

In order to be able to execute independently each folder of this tutorial (3_notebooks, 4_modularization etc) although the code is the same, we rename `src` from directory `5_scripting` to `src_debug` in `6_debugging` as otherwise there would be a name conflict. We therefore install it as an additional package

in `path/to/6_debugging`

        python3 -m pip install -e .

## Option 1: using pdb
If you take a look at `path/to/6_debugging/src_debug/load.py:load_iris_df`, an method from an extra library was imported at the top: `pdb.set_trace`. Pdb is the python debugger, and lets you trigger an interactive environment to examine variables etc.

First try executing the `load_iris_df` method in an interactive python shell


         python3
         >> from src_debug.load import load_iris_df
         >> load_iris_df
         >> (IndexError): Index out of range....

Now, uncomment the line 13 of `load.py` ( the `set_trace` statement) and try again

         python3
         >> from src_debug.load import load_iris_df
         >> load_iris_df

A command prompt starting with `(Pdb)` appears, the fun can begin!

Here are the most useful pdb commands

* `l(ist)`: show where you are in the code
* `n(ext)`: jump to the next line
* `s(tep)`: step into the function called at the current line
* `c(ontinue)`: execute until a breakpoint is encountered
* `q(uit)`: exit the debugger

In our case we can for instance run
    
     >> print(column_names)

to realize that `column_names` has not 30 elements.

## Option 2: using the %debug in a jupyter notebook

cf path/to/6_debugging/notebooks/iris_debug.ipynb` for guidelines :)
