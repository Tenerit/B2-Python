#!/usr/bin/python36
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
while nombre != nbrMyst:
    nbrcoup += 1
    print("Trouve le nombre mystère")
    nombre = input()
    nombre = int(nombre)
 
    if nombre < nbrMyst:
        print("Le nombre mystère est plus grand !\n")
 
    elif nombre > nbrMyst:
        print("Le nombre mystère est plus petit !\n")


    elif str(nombre) == "q":
        break
 
    else:
        print("Félicitations, vous avez trouvé le nombre mystère !!!")
        print ("Qui étais", int(nbrMyst))
        print ("En", int(nbrcoup), "coups")
 
