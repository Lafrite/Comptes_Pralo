#!/usr/bin/env python
# encoding: utf-8


class Account(object):
    """@todo"""

    def __init__(self, account):
        """Initiate the account as a list

        :param account: list of tuples (length 2 with name and credit) [("bob", 4), ("hip",2)...]

        """
        self._account = account
        
    def tribut(self, seuil = 0):
        """Tels who owns what to who (recursive algorithm

        :param seuil: seuil à partir duquel on ne doit plus rien.
        :return: liste des valeurs associées aux débits des comptes après le remboursement
        """
        self._account.sort(key = lambda s: s[1])
        m = self._account[0]
        M = self._account[-1]

        res = ['doneur','receveur',0]
    
        # Si celui qui doit le plus doit moins que le crédit que celui qui a le plus grand crédit
        # Il va donc tout lui donner
        if  abs(m[1]) <= abs(M[1]):
            M2 = M[1] + m[1]
            # print("{em} donne {em_n} à {eM} donc {em} devient {eM2}".format(em = m[0], em_n = abs(m[1]), eM = M[0] , eM2 = M2)) 
            res = [m[0], M[0], abs(m[1])]
            # On enleve le minimum
            self._account.remove(m)
            # ON change la valeur du max
            self._account[-1] = [M[0],M2]
        
        # Sinon il donne juste de quoi compenser
        else:
            m2 = m[1] + M[1]
            # print("{em} donne {eM_n} à {eM} et devient {em2}".format(em = m[0] , em2 = m2 , eM = M[0], eM_n = M[1]))
            res = [m[0], M[0], abs(M[1])]
            # On eleve le max
            self._account.remove(M)
            # On change la valeur du min
            self._account[0] = [m[0], m2]

        # Gestion du Seuil
        self._account = [i for i in self._account if abs(i[1]) >= seuil]
    
        if (len(self._account) > 1):
            #print(self._account)
            return [res] + self.tribut(seuil=seuil)
        else:
            return [res]

    def __add__(self, account):
        pass

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
