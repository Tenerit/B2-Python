#!/usr/bin/env python36
# 3b-opt
# Script qui permet d'effectuer une sauvegarde.
# 11/11/18
# Scotto Anthony

# Importe des modules
import signal
import shutil
import gzip
import os
import sys
import subprocess


# Fonction qui cree une archive
def createArchive():
    os.remove(path_data + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', path_data)


# Fontion qui supprime l'archive déjà existante
def supprArchive():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')


# Fonction qui quitte le prog
def end(sig, frame):
    supprArchive()
    sys.exit(0)


signal.signal(signal.SIGINT, end)

#Les Variables
path_data = os.path.expanduser('~/data/')
path_directory = os.path.expanduser('~/B2-Python/scripts')
archive = os.path.expanduser('~/archive')
disk_capacity = os.system("df -h | grep '%s'")


#Si l'archive existe sinon on la crée
try:
    os.makedirs(path_data, exist_ok=True)
except OSError:
    if not os.path.isdir(path_data):
        raise



# On vérifie qu'il reste plus de 5 Go de libre
if disk_capacity > 3:

    # On regarde si on a les permissions W & R
    if os.access(path_data, os.W_OK and os.R_OK):

        # On crée l'archive
        shutil.make_archive(archive, 'gztar', path_directory)

        # On regarde si une ancienne save existe
        if os.path.exists(path_data + '/archive.tar.gz'):

            # On va lire à l'interieur de la save existante
            with gzip.open(path_data + '/archive.tar.gz', 'rb') as f:
                exist_save = f.read()
            # On va lire la nouvelle save maintenant
            with gzip.open(archive + '.tar.gz', 'rb') as f:
                new_save = f.read()

            # On compare les deux save
            if exist_save != new_save:
                # On supprime l'ancienne et on sauvegarde la nouvelle
                createArchive()
                sys.stdout.write('La sauvegarde a été effectuer correctement\n')

            else:
                supprArchive()
                sys.stdout.write('Oopsy, il semblerait que la sauvegarde existe déjà\n')

        else:
            shutil.move(archive + '.tar.gz', path_data)
            sys.stdout.write('La sauvegarde a été effectuer correctement\n')

    else:
        sys.stderr.write('Il semblerait que vous ne disposiez pas des droits sur le répertoire de destination\n')

else:
    sys.stderr.write('Il n\'y a pas assez d\'espace libre')
