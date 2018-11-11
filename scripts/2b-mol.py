#!/usr/bin/env python36
# 1d-mol
# jeu du plus ou moins dans un fichier
# 24/10/2018
# Scotto Anthony et Borie Florien

# Importe des modules
import signal
import random
import re
import time

# on créé la fonction de fin
def fin():
    print("j'ai trouver "+str(rep)+" en "+str(count))
    
# on créé la fonction pour lire dans le fichier
def read_file():
    file = open("jeu.txt", "r")
    msg = file.read()
    file.close()
    return msg

# on créé la fonction pour écrire dans un fichier
def write_file(msg):
    file = open("jeu.txt", "w")
    file.write(msg)
    file.close()


# on créé les variables nécessaires
solution = random.randint(0, 100)
end = False
count = 0
borneSup = 100
borneInf = 0
rep = 0


# on initialise la boucle pour le jeu
while end is False:

    print("borne sup : " + str(borneSup) + " borne inf : " + str(borneInf))

    rep = round((borneSup + borneInf) / 2)
    write_file(str(rep))
    count += 1
    print(rep)
    time.sleep(3)
    saisie = read_file()
    print("data : " + data)

    if saisie == "Bien jouer":
        end = True
        print("Good job, tu as gagner")

    elif saisie == "You win":
        borneSup = rep
        print("Trop grand")

    elif saise == "Trop petit !":
        borneInf = rep
        print("Trop petit")
fin()
