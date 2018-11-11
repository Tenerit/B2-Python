#!/usr/bin/python3.6
#1c-moy.py
#Demande une saisie utilisateur de plusieurs notes et prénoms
#Scotto Anthony
#15/10/2018

#importation
import operator

#un system de variables <3 <3 <3
dict = {}
tour = 0
sum = 0
note = 0

#un system d'input
def inputNote():
  note = input('Entrez une note : ')
  #system de verification que la note soit bien un nombre
  while(note.isdigit() == False):
     note = input('Entrez une note qui soit un nombre svp: ')
  return int(note)

  #system de verification que le prenom soit bien une lettre
def checkPrenom():
   prenom = input('Entrez un prénom : ')
   while(prenom.isalnum() == False):
    prenom = input('Entrez un prenom avec des lettres svp : ')
   return str(prenom) 



#le petit boucle des familles
while tour == 0:
     prenom = checkPrenom()
    #Si l'on appuie sur q pour valider et sortir les resultat.
     if prenom == "q":

        #petit ajout qui t'emoustille
        for liste in sorted(dict):
            full = dict[liste]
            print(full)
            sum += int(full)
            
        #lee Calcoule de le notes   
        print("Votre moyenne est égale a : ")
        moy = sum / len(dict)
	#i le resutate arondie
        print(int(moy))
        print("Voici les notes :")
	#la fonction magique qui recup les 5 premiers notes
        print(sorted(dict.items(), key=operator.itemgetter(1), reverse = True)[:5])
        break
    
     else:
	#lee saisi prenom et note
        note = inputNote()
        dict[prenom] = note

