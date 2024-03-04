Mostly a proof of concept in order to "play" with pytest

Otherwise ./src/main shows how to multiply or add 4 binary operands using only NAND gates


### THE key for me was
To use the command ```python -m pytest``` rather than the short command ```pytest```.


Just to make sure it is crystal clear : 
1. Open the project in VSCode
1. Make sure you can run/debug main.py for example
1. Open a terminal within VSCode
1. You should be at the top of the project directory
1. In the terminal, type ```python -m pytest``` then strike ```ENTER```


### Keep in mind 
* ```pytest``` command does not add the current path to PYTHONPATH, which means that the modules tested may not be importable.
* If necessary, make sure to update ```PYTHONPATH``` **before** using the short command (aka ```pytest```).


```
PYTHONPATH=$PYTHONPATH:.
pytest
```


About ```__init__.py``` 
* https://medium.com/towards-data-science/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355
* https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
* see ```__init__.py``` in src/ sub-directories for example

For directories organisation 
* https://github.com/AutomationPanda/python-testing-101/tree/master

