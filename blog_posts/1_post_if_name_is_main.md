
## ``` if "__name__" == "__main__" ```

How many times have you seen this awkward syntax and postponed understanding it? Or maybe you simply memorized it? This is no longer needed, because I have set up a simple example and a step-by-step explanation on what this means, when and how to use it. 

### a. Scenario
In order to figure out what's the deal with this weird syntax, let's first create a simple architecture with two python files:
- utils.py (where some useful functions are kept)
```
def calculate_sum(first: int, next: int)-> int:
    added = first + next
    return added

def test_calculate_sum():
    assert(calculate_sum(3,8)==11)
    assert(calculate_sum(-3,8)==5)
    assert(calculate_sum(-1,0)==-1)

test_calculate_sum()
summed = calculate_sum(4,6)
print(summed)

print(globals())
```
- app.py (the code to run our app)
```
from utils import calculate_sum

result = calculate_sum(10,100)
print(result)

print(globals())
```
utils.py acts as a sort of collection of functions, from were one can pick and use them in other parts of the application.\
Because both files are python files, they are self-sufficient and can be executed separately with:
```
> python utils.py
> python app.py
```
### b. Global variables
Python comes with a pre-defined set of global variables. Besides those, all other variables we declare outside the functions we create are added to the list of global variables, when the program is executed. The global variables are visible to the user through the command ```globals()```. In this dictionary of default globals is where one finds the syntax ```{'__name__': '__main__', ...}```. Therefore, ```__name__``` is a global variable.

Checking the global variable of the two python files proves that for both files, ```{'__name__': '__main__'}```.\
app.py is dependent on utils.py, as it requires a function defined in the latter. Let's trace how is this dependency materialized, by only executing app.py.\
Inspecting the globals after running app.py shows that other variables were added to the default list, ```"summed:..., "result":...``` and besides that, the ```print()``` was executed in both app.py and utils.py, displaying the results. So even if only needing one function defined in a separate file, through importing the utils module in app.py the entire utils.py was executed. 

### c. ... so how should we improve this?
This syntax comes in handy when importing a python file as a module, specifically when wanting to use the function from utils.py in app.py. In this situation, executing the code in the file that is being imported as a module is non-sense, as it should be used simply as a collection of functions from where to select and use further.

Adding the syntax ```if "__name__" == "__main__"```, before calling the functions in utils.py, acts as a limit that tells the python interpreter to only move forward if the file is executed alone, by itself, otherwise stop. 
This will result in a change of the value in the utils.py globals() to ```{'__name__': 'name_of_module'}```, each time the file is imported as a module.(*here, <i>name_of_module</i> is utils).\
Let's see how utils.py looks like, after adding this piece of code:

```
def calculate_sum(first: int, next: int)-> int:
    added = first + next
    return added

def test_calculate_sum():
    assert(calculate_sum(3,8)==11)
    assert(calculate_sum(-3,8)==5)
    assert(calculate_sum(-1,0)==-1)

# Adding this line will tell the interpretor to NOT execute the next lines when importing this file as a module.
if "__name__" == "__main__":
    test_calculate_sum()
    summed = calculate_sum(4,6)
    print(summed)

# print(globals())
```
### d. Closing remarks
A python file can be used both in its own right and as a module, so this weird syntax is just a way to communicate your intentions to the python interpreter, with the purpose being efficient and not execute needless code.
