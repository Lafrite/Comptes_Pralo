Comptes Pralo
=============

Outils codé rapidemenet pour faire les comptes en fin de séjour.

Utilisation
-----------

On écrit ce que chacun à payé au long du séjour et on renseigne le temps de séjour pour chaque personne dans un fichier .csv .

compte_test.csv::

    nom,montant, jours
    pipo,   23, 3
    hiphop, 40, 4
    chic,   0, 4
    Couette,50, 1

Puis on fait tourner le programme sur le fichier::

    > pralo.py -f compte_test.csv

    Cout total de Pralo: 113
    Le nombre de jour passé 12
    Cout au jour: 9.42


    chic donne 37.67 à Couette
    pipo donne 2.92 à Couette
    pipo donne 2.33 à hiphop

