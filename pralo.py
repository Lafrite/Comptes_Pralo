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
    l.sort() 
    m = l[0]
    M = l[-1]
 
    # Si celui qui doit le plus doit moins que le crédit que celui qui a le plus grand crédit
    # Il va donc tout lui donner
    if  abs(m) <= abs(M):
        M2 = M + m
        print("{em} donne tout à {eM} donc {em} devient {eM2}".format(em = m ,eM = M , eM2 = M2)) 
        # On enleve le minimum
        l.remove(m)
        # ON change la valeur du max
        l[-1] = M2
       
    # Sinon il donne juste de quoi compenser
    else:
         m2 = m + M
         print("{em} donne {eM} à {eM} et devient {em2}".format(em = m , em2 = m2 , eM = M))
         # On eleve le max
         l.remove(M)
         # On change la valeur du min
         l[0] = m2
 
    if (len(l) > 1):
        print(l)
        echange(l)

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    
    # État des comptes
    compte = [123 , 145 , 43 , 89 , 0]
    moyenne = sum(compte) / len(compte)
    compte_normalise = [c - moyenne for c in compte]
    print(compte_normalise)

    echange(compte_normalise)
# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

