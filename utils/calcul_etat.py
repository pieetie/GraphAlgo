def calcHisto(valeur_depart, ancienne_valeur, historique):
    """
    Renvoie un indice (sur 100) de l'état de la valeur de l'action dans le temps (temps donné t) grâce à l'historique

    50 : état normal
    100 : état amélioré
    0 : état diminué 
    """
    etat = 50
    
    if len(historique) < 10:
        moyenne_totale = sum(historique.values()) / len(historique)
        moyenne_dix = (ancienne_valeur + valeur_depart)/2
    else :
        dix_dernieres_valeurs = list(historique.values())[-10:]
        
        moyenne_totale = sum(historique.values()) / len(historique)
        moyenne_dix = sum(dix_dernieres_valeurs) / len(dix_dernieres_valeurs)

    #conditions
    if moyenne_totale >= valeur_depart:
        etat += 15
    else:
        etat -= 15

    if moyenne_dix >= valeur_depart:
        etat += 25
    else:
        etat -= 25

    if ancienne_valeur >= valeur_depart:
        etat += 10
    else:
        etat -= 10

    return etat

def calcEtat(valeur_depart, ancienne_valeur, historique, probaNormale):
    """
    Permet de calculer la probabilité de hausse ou de baisse pour la prochaine valeur
    """
    seuil = 1 - probaNormale
    etat = calcHisto(valeur_depart, ancienne_valeur, historique)
    #print(f"l'état est de : {etat}")
    
    ajustement = 0
    if etat < 50:
        if etat == 30:
            ajustement = 0.005
        elif etat == 20:
            ajustement = 0.01
        else:
            ajustement = 0.10
    elif etat > 50:
        if etat == 70:
            ajustement = -0.005
        elif etat == 80:
            ajustement = -0.01
        else:
            ajustement = -0.10
    
    proba_baisse = round( ((1 - probaNormale) / 2) + (ajustement * seuil), 3)
    proba_hausse = round( ((1 - probaNormale) / 2) - (ajustement * seuil), 3)

    return proba_baisse, proba_hausse