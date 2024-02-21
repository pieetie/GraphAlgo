#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import random

from utils import *

def calcul(jour, totjours, fxFaillite, fxReussite, taux, valeur_depart, ancienne_valeur, probaNormale, n_annees, historique):
    """
    Fonction de calcul principale
    """
    taux_journee = taux*n_annees / totjours #si tout ce passe bien, au bout d'un an on aura le taux annuel appliqué (si 100% probaNormale)
    
    if probaNormale == 1:
        nouvelle_valeur = ancienne_valeur * (1+taux_journee)
    else:
        proba_baisse, proba_hausse = calcEtat(valeur_depart, ancienne_valeur, historique, probaNormale)
        choix = tirage(probaNormale, proba_baisse, proba_hausse)
        #print(choix)

        if choix == "Baisse":
            nouvelle_valeur = baisse(ancienne_valeur)
        elif choix == "Hausse":
            nouvelle_valeur = hausse(ancienne_valeur)
        else:
            nouvelle_valeur = ancienne_valeur * (1+taux_journee)
        
    return nouvelle_valeur

def main():
    """
    Fonction principale
    """

    """Valeurs par défaut que j'ai utilisé dans le notebook Jupyter (archives)"""
    annee_classique = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    annee_bissextile = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    valeurs = [] #liste qui va stocker nos valeurs (points sur l'axe X à placer)
    annees = [] #liste qui va stocker les différentes années
    historique = {} #dictionnaire jour-valeur

    valeur_depart = 100 #valeur par défaut
    f_reussite = 1 #facteur chance réussite
    f_faillite = 1 #facteur chance faillite
    taux = 0.05 #5% en moyenne
    probaNormale = 0.50 #50%

    start_annee = 2024
    fin_annee = 2027


    """Initialisation - Entrée des valeurs de départ"""
    start_annee = 2024
    fin_annee = 2029

    valeur_depart = 100
    f_reussite = 1
    f_faillite = 1
    taux = 0.05
    probaNormale = 0.40

    """Lancement de la création du graphique"""
    annees, n_annees, n_mois, jours_ans, n_jours = logiqueAnnee(start_annee, fin_annee)
    compteur = 0
    valeurs.append(valeur_depart)

    historique = {}
    historique[0]= valeur_depart

    for i in range(1,n_jours+1):
        if compteur == 0:
            ancienne_valeur = valeur_depart
            valeurs.append(calcul(i, n_jours, f_faillite, f_reussite, taux, valeur_depart, ancienne_valeur, probaNormale, n_annees, historique))
            historique[i]= valeurs[i]
        else:
            ancienne_valeur = valeurs[i-1]
            valeurs.append(calcul(i, n_jours, f_faillite, f_reussite, taux, valeur_depart, ancienne_valeur, probaNormale, n_annees, historique))
            historique[i]= valeurs[i]
        compteur += 1

    #print(historique)
    #print("#####")
    #print(valeurs)
    #en gros x représente les jours alors que y représente les valeurs boursières
    x = range(1,n_jours+1+1) #+1 car on prend 0 au départ comme valeur de depart
    y = valeurs

    plt.plot(x, y)
    #plt.title("Représentation graphique de l'évolution d'un titre sur 1 année")
    plt.xlabel("Jours")
    plt.ylabel("Valeurs")

    plt.show()

if __name__ == "__main__":
    main()