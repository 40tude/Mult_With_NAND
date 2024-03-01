**LA** clé c'est, depuis la racine du projet, d'utiliser la commande :

```python -m pytest```

Versus : 
```pytest```

* En effet, la commande "pytest" n'ajoute pas le chemin actuel à PYTHONPATH, ce qui signifie que les modules testés peuvent ne pas être importables.
* Si besoin assurez-vous de mettre à jour PYTHONPATH avant d'utiliser les commandes courtes.

```
PYTHONPATH=$PYTHONPATH:.
pytest
```

A propos de "__init__.py" 
Lire : https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html


Pour l'organisation des répertoires 
Lire : https://github.com/AutomationPanda/python-testing-101/tree/master
