Mostly a proof of conscept in order to "play" with pytest

Otherwise ./src/main shows how to multiply or add 4 binary operand using only NAND gates


**THE** key is to use the command :

```python -m pytest```

Versus : 
```pytest```

* Indeed, the "pytest" command does not add the current path to PYTHONPATH, which means that the modules tested may not be importable.
* If necessary, make sure to update PYTHONPATH before using the short commands.

```
PYTHONPATH=$PYTHONPATH:.
pytest
```


About ```__init__.py``` 
* Read: https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html


For directories organisation 
* Read: https://github.com/AutomationPanda/python-testing-101/tree/master
* ```__init__.py``` in src/ sub-directories
