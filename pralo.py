#! /usr/bin/env python
# 

# ------------------------------
# 
# La grosse fleme de faire les comptes à chaque fois
# Maintenant c'est toi qui les fait pour moi :D
#
# ------------------------------


# ------------------------------
# Imports
# ------------------------------ 
import csv
import os
import optparse

# ------------------------------
# Classes
# ------------------------------ 

# ------------------------------
# Fonctions
# ------------------------------ 
def extrait_from_file(file_name):
    """Extrait les informations à partir d'un fichier"""
    file = open(file_name, "r")
    try:
        reader = csv.reader(file, delimiter = ",")
        compte =  list(reader)
        for i in compte[1:]:
            i[1] = float(i[1])
            i[2] = float(i[2])
        return compte
    finally:
        file.close()


def echange(l):
    """Algo recursif pour gérer les échanges"""
    l.sort(key = lambda s: s[1])
    m = l[0]
    M = l[-1]

    res = ['doneur','receveur',0]
 
    # Si celui qui doit le plus doit moins que le crédit que celui qui a le plus grand crédit
    # Il va donc tout lui donner
    if  abs(m[1]) <= abs(M[1]):
        M2 = M[1] + m[1]
        # print("{em} donne {em_n} à {eM} donc {em} devient {eM2}".format(em = m[0], em_n = abs(m[1]), eM = M[0] , eM2 = M2)) 
        res = [m[0], M[0], abs(m[1])]
        # On enleve le minimum
        l.remove(m)
        # ON change la valeur du max
        l[-1] = [M[0],M2]
       
    # Sinon il donne juste de quoi compenser
    else:
         m2 = m[1] + M[1]
         # print("{em} donne {eM_n} à {eM} et devient {em2}".format(em = m[0] , em2 = m2 , eM = M[0], eM_n = M[1]))
         res = [m[0], M[0], abs(M[1])]
         # On eleve le max
         l.remove(M)
         # On change la valeur du min
         l[0] = [m[0], m2]
 
    if (len(l) > 1):
        #print(l)
        return [res] + echange(l)
    else:
        return [res]

def forfait(compte):
    """Gère le nombre resté à Pralo"""
    cout_total = sum([c[1] for c in compte])
    print("Cout total de Pralo: {cout_tot}".format(cout_tot = cout_total))

    nbr_jour = sum([c[2] for c in compte])
    print("Le nombre de jour passé {njour}".format(njour = nbr_jour))

    cout_jour =  cout_total / nbr_jour
    print("Cout au jour: {cout}".format(cout = cout_jour))

    print("\n")

    new_compte = []
    for pers in compte:
        new_compte += [[pers[0], (pers[1] - pers[2] * cout_jour)]]
    return new_compte

def normalise(compte):
    """Centre en 0 les comptes"""
    moyenne = sum([c[1] for c in compte]) / len(compte)
    compte_normalise = compte

    for (i,n) in enumerate(compte):
        compte_normalise[i][1] = compte[i][1] - moyenne

    return compte_normalise


def affiche_final(donRec):
    """Affiche qui donne quoi à qui à partir de la liste"""
    for g in donRec:
        print("{don} donne {montant} à {rec}".format(don = g[0], rec = g[1], montant = g[2]))


def elimine_seuil(liste, seuil):
    """Elimine les éléments de la liste qui sont sous le seuil """
    pass


# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    # Pour analyser les options qu'on lui demande 
    parser = optparse.OptionParser()
    # options proposée
    parser.add_option("-f","--file",action="store", type = "string", dest="file_name", help="Analyse les comptes à partir du fichier donné en argument")
    # Digestion
    (options, args) = parser.parse_args()

    if options.file_name:
        compte = extrait_from_file(options.file_name)[1:]
        # compte_normalise = normalise(compte)
        compte_normalise = forfait(compte)
        final = echange(compte_normalise)
        affiche_final(final)

# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

