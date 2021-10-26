#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import cmath
import turtle
from typing import Tuple

# TODO: Définissez vos fonction ici
1.
def calculer_volume_et_masse(a=2,b=4,c=6,p=10)-> Tuple:
    V=(cmath.pi*a*b*c)*(4/3)
    m=p*V
    return V,m
4.
def valider_ADN(string):
    acides_aminés=["a","t","g","c"]
    if len(string) == 0:
        return False
    for i in string:
        if i in acides_aminés:
            continue
        else:
            return False
    return True

def retourner_chaine(saisie):
    string=saisie
    if valider_ADN(string):
        return string
    else:
        return f"La chaine {saisie} n'est pas valide"
    return retourner_chaine(saisie)

def proportion(chaine,sequence):
    proportion=100*chaine.count(sequence)/len(chaine)
    return proportion
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a=input("Écrire une séquence d'ADN: ")
    b=input("Écrire une chaine d'ADN: ")
    print(calculer_volume_et_masse())
    print(f"chaîne : {b}")
    print(f"séquence : {a}")
    print(f"Il y a {proportion(b,a)}% de '{a}'. " )
    pass
