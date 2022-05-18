# 2. Notebooks limitations

## Reproducibility
Try executing the notebook sequentially: obviously the notebook is not reproducible, probably because the last person who worked on it did not make sure to execute it sequentially. This problem does not exist with python scripts, as the control flow is not user dependant once the script start getting executed.

## Version control
Modify a few cells in the notebook `iris.ipynb` and save the corresponding changes. Now, try to run

         git diff iris.ipynb

As notebooks are html documents, the output is way too verbose, it is hard to see what changes between the files
(some extensions in vscode handle this case)

## Modularity
Finally, this is not illustrated here for convenience, but you probably already ran into the hassle of notebooks of a few hundreds cells, where keeping tracks of the controls flow and all local variables can quickly become pretty messy.

## Solution
We will now see solutions to start structuring our code, which will on the long term make us gain clarity and efficiency :D
