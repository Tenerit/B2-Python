#!/usr/bin/python36
#2a-mol.py
#Jeu du plus ou moins qui lit dans un fichier
#Développé par Anthony Scotto Et Florian Borie
#24/10/2018

import os
from random import randrange

import signal
from time import sleep

def youcant(sig, frame):
    print('You cant CTRL+C on me !')

signal.signal(signal.SIGINT, youcant) 


nombre = 0
 
print("LE JEU DU PLUS OU MOINS \n")
 
nbrMyst = randrange(1, 100)
nbrcoup = 1

#ouverture fichier ecriture et lecture
f = open('2a-molB.txt', 'w',)
f.write("Bienvenue \n")
f.close()

#boucle infini
while nombre != nbrMyst:
    nbrcoup += 1
    print("Trouve le nombre mystère")
    nombre = input()
#stockage du nombre myst dans un fichier txt et lecture de la dernier ligne
    f = open('2a-molB.txt', 'a',)
    f.write(str(nombre))
    f.close()
    f = open('2a-molB.txt', 'r',)
    x=f.readlines()[-1]

#si le nombre myst est plus grand  
    if int(nombre) < nbrMyst:
        print("Le nombre mystère est plus grand !\n")
#si le nombre myst est plust petit
    elif int(nombre) > nbrMyst:
        print("Le nombre mystère est plus petit !\n")

#pour stopper linput
    elif str(x) == "q":
        break
#si nous avons gagner 
    else:
        print("Félicitations, vous avez trouvé le nombre mystère !!!")
        print ("Qui étais", int(nbrMyst))
        print ("En", int(nbrcoup), "coups")
        f = open('2a-molB.txt', 'w',)
        f.write("")
        f.close()
        break

