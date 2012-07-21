#/usr/bin/env python
#-*- coding:utf-*-
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

# ------------------------------
# Classes
# ------------------------------ 
class Pralo():
    """Pour faire ses comptes quand on part avec ses copains"""
    def __init__(self,  ):
        super(Pralo, self).__init__()
        
    def open_file(self, file):
        """Récupere les informations depuis un fichier CSV"""
        pass

    def best_repart(self, e = 0):
        """Calcul qui doit qui à qui en minimisant les échanges avec e la marge d'erreur"""
        pass

    def print_bilan(self):
        """Affiche le rendu des échanges"""
        pass
        

# ------------------------------
# Fonctions
# ------------------------------ 

def echange(l):
    """Algo recursif pour gérer les échanges"""
    l.sort(key = lambda s: s[1])
    m = l[0]
    M = l[-1]
 
    # Si celui qui doit le plus doit moins que le crédit que celui qui a le plus grand crédit
    # Il va donc tout lui donner
    if  abs(m[1]) <= abs(M[1]):
        M2 = M[1] + m[1]
        print("{em} donne {em_n} à {eM} donc {em} devient {eM2}".format(em = m[0], em_n = abs(m[1]), eM = M[0] , eM2 = M2)) 
        # On enleve le minimum
        l.remove(m)
        # ON change la valeur du max
        l[-1] = [M[0],M2]
       
    # Sinon il donne juste de quoi compenser
    else:
         m2 = m[1] + M[1]
         print("{em} donne {eM_n} à {eM} et devient {em2}".format(em = m[0] , em2 = m2 , eM = M[0], eM_n = M[1]))
         # On eleve le max
         l.remove(M)
         # On change la valeur du min
         l[0] = [m[0], m2]
 
    if (len(l) > 1):
        #print(l)
        echange(l)


def normalise(compte):
    """Centre en 0 les comptes"""
    moyenne = sum([c[1] for c in compte]) / len(compte)
    compte_normalise = compte
    for (i,n) in enumerate(compte):
        compte_normalise[i][1] = compte[i][1] - moyenne
    return compte_normalise


# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    
    # État des comptes
    compte = [['bob', 123] , ['pipo', 145] , ['hiphop', 43] , ['dede', 89] , ['chic', 0]]
    compte_normalise = normalise(compte)
    print(compte_normalise)

    echange(compte_normalise)
# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

