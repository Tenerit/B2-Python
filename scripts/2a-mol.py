#!/usr/bin/env python36
# 2a-mol
# Jeu du plus ou moins dans un fichier
# 23/10/2018
# Scotto Anthony et Borie Florien

#Importe des modules
import signal
import random
import re

# fonction anti ctrlC
def stop_ctrlC(sig, frame):
   fin()


signal.signal(signal.SIGINT, stop_ctrlC)
# on créé la fonction de fin


def fin():
    print("\b Au revoir")
    exit()


# la fonction pour écrire dans un fichier
def write_file(msg):
    file = open("plusoumoins.txt", "w")
    file.write(msg)
    file.close()

# on créé la fonction de lecture du fichier
def read_file():
    file = open("plusoumoins.txt", "r")
    msg = file.read()
    file.close()
    return msg


#Variables du regex; du nbr mytere et de la fin
regx = re.compile('^[0-9]+')
nbr_myst = random.randint(0, 100)
end = False


print("Bienvenue dans le jeu du plus ou moins")
write_file("Veuillez entrez un chiffre entre 0 et 100")

# mise en place d'une boucle
while end is False:
    # Lecture du fichier et affectation dans la variable saisie
    saisie = read_file()
    # On vérifie que la variable saisie est un nombre
    if regx.match(saisie):
        saisie = int(saisie)
        
#comparaison de la saisie avec le nombre mystere
        if saisie > nbr_myst:
            write_file("Trop grand !")

        elif saisie < nbr_myst:
            write_file("Trop petit !")
        # Fin du jeu et fin de la boucle

        else:
            write_file("You win")
            end = True
            fin()
