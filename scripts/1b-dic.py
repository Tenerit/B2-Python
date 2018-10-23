#!/usr/bin/python36
#1c-moy.py
#Demande une saisie utilisateur de plusieurs prénom qui seront afficher
#dans l'ordre alphabetique
#Développé par Anthony Scotto Et Florian Borie
#15/10/2018

entree_list=[]
element=""

import re
reg = re.compile('^[a-zA-Z]+$')
while entree_list != "":
    print("------ Appuyer sur q pour terminer la saisie ------")
    element=input("Taper un mot : ")
    if reg.match(element):
     entree_list.append(element)

     if element == 'q':
           break

    else:
         print("ce n'est pas un nombre")  
 
entree_list=entree_list[:-1]
entree_list=sorted(entree_list)
print(entree_list)

print("*** Fin ***")
input("Appuyer sur ENTER pour terminer le programme. ")
