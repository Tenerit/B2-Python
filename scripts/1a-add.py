#!/usr/bin/python36
#1a-add.py
#Demande deux nombres a l'utilisateur pour afficher l'addition des deux nombres
#Scotto Anthony
#15/10/2018

#system d'import
import re
import time
#on écrit les deux nombres
print("choisi un nombre")
value1 = input()
print("choisi un autre nombre")
value2 = input()
#le regex
reg = re.compile('^[0-9]+')

value1 = int(value1)
value2 = int(value2)

print("leurs somme est égale a ")
#On vérifie si ler valeur sont des nombres
if reg.match(str(value1)) and reg.match(str(value2)):
#La fameuses addition
  print(int(value1) + int(value2))
else:
  print("Ce ne sont pas des nombres")

#On ajoute un délai pour le fun
time.sleep(2)
