def njAnnee(annee):
    """
    Retourne 366 si l'année est bissextile 
    Retourne 365 l'année est classique

    Règles :
    - une année est bissextile si elle est divisible par 4.
    - si elle est divisible par 100 elle n'est pas bissextile sauf si elle est divisible par 400.
    """
    if annee % 400 == 0:
        return 366
    elif annee % 100 == 0:
        return 365
    elif annee % 4 == 0:
        return 366
    else:
        return 365
    
def logiqueAnnee(debut, fin):
    """
    Logique de calcul pour les différentes variables en lien avec les années, etc...
    """
    annees = [annee for annee in range(debut,fin)] #l'année de fin n'est pas incluse
    n_annees = len(annees)
    n_mois = n_annees * 12
    jours_ans = [njAnnee(annee) for annee in annees]
    n_jours = sum(jours_ans)
    return annees, n_annees, n_mois, jours_ans, n_jours