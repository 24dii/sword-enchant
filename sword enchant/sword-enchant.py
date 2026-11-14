import inquirer 
import time
import os
import random
import sys

language = [
    inquirer.List('choice',
                  message="language",
                  choices=['KO','EN']
                  )
]
choice = inquirer.prompt(language)
if choice['choice'] == 'KO':
    import KO
else:
    import EN