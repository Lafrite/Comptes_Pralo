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

from account import Account

# ------------------------------
# Classes
# ------------------------------ 

# ------------------------------
# Fonctions
# ------------------------------ 
def extrait_from_file(file_name):
    """
    Extrait les informations à partir d'un fichier
    
    :param file_name: nom du fichier avec les comptes 
    :return: liste [[nom,montant,jours],...]
    """
    file = open(file_name, "r")
    try:
        reader = csv.reader(file, delimiter = ",")
        r_comptes =  list(reader)
        header = r_comptes.pop(0) # On récupère le premier élément (les headers)

        comptes = []

        for c in r_comptes: # On parcourt les lignes pour typer les éléments correctement
            compte = {}
            for (i,h) in enumerate(header):
                if "nom" in h.lower():
                    compte["nom"] = c[i]
                if "montant" in h.lower():
                    compte["montant"] = eval(c[i])
                if "jour" in h.lower():
                    compte["jours"] = int(c[i])
            comptes += [compte]

        return comptes
    finally:
        file.close()



def forfait(compte):
    """
    Gère le nombre resté à Pralo
    
    :param compte: comptes de ce que chacun a payé [[nom, montant,jours],...]
    :return: Comptes des crédits de chacun envers la communauté
    """
    cout_total = sum([c["montant"] for c in compte])
    print("Cout total de Pralo: {cout_tot}".format(cout_tot = cout_total))

    nbr_jour = sum([c["jours"] for c in compte])
    print("Le nombre de jour passé {njour}".format(njour = nbr_jour))

    cout_jour =  cout_total / nbr_jour
    print("Cout au jour: {cout}".format(cout = round(cout_jour,2)))

    print("\n")

    new_compte = []
    for pers in compte:
        new_compte += [[pers["nom"], (pers["montant"] - pers["jours"] * cout_jour)]]
        
    return new_compte

def normalise(compte):
    """Centre en 0 les comptes"""
    moyenne = sum([c["montant"] for c in compte]) / len(compte)
    compte_normalise = compte

    for (i,n) in enumerate(compte):
        compte_normalise[i]["montant"] = compte[i]["montant"] - moyenne

    return compte_normalise


def affiche_final(donRec):
    """
    Affiche qui donne quoi à qui à partir de la liste
    
    :param donRec: liste avec qui doit quoi à qui [[qui, àqui, quoi]...]
    """
    for g in donRec:
        print("{don} donne {montant} à {rec}".format(don = g[0], rec = g[1], montant = round(g[2],2)))


# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    # Pour analyser les options qu'on lui demande 
    parser = optparse.OptionParser()
    # options proposée
    parser.add_option("-f","--file",action="store", type = "string", dest="file_name", help="Analyse les comptes à partir du fichier donné en argument")
    parser.add_option("-e","--seuil",action="store", type = "int", dest="seuil",default=0, help="Seuil à partir duquel on concidère qu'il n'est plus nécessaire de payer.")
    # Digestion
    (options, args) = parser.parse_args()

    if options.file_name:
        compte = extrait_from_file(options.file_name)
        # compte_normalise = normalise(compte)
        compte_normalise = forfait(compte)
        #final = echange(compte_normalise, options.seuil)
        account = Account(compte_normalise)
        final = account.tribut(options.seuil)
        affiche_final(final)

# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

