import random
import numpy as np

def hausse(ancienne_valeur):
    """
    dépend largement des conditions de marché et de l'entreprise
    probabilités à changer en fonction du type d'action...
    (à compléter)
    """ 
    probabilite_hausse_significative = 0.001
    probabilite_hausse_moderee = 0.005
    probabilite_hausse_legere = 1 - probabilite_hausse_significative - probabilite_hausse_moderee

    options = ["Hausse légère", "Hausse modérée", "Hausse significative"]
    probabilites = [probabilite_hausse_legere, probabilite_hausse_moderee, probabilite_hausse_significative]

    selection = random.choices(options, weights=probabilites, k=1)[0]

    if selection == "Hausse légère":
        #hausse légère de 0.01% à 1%
        gains = [round(x, 2) for x in np.linspace(0.01, 1, 499+1)]
        proba_gains = [random.uniform(0.5, 1) for _ in gains]
        proba_gains = [p/sum(proba_gains) for p in proba_gains]

        gain_selectionne = random.choices(gains, weights=proba_gains, k=1)[0]

    elif selection == "Hausse modérée":
        #hausse modérée de 1% à 10%
        gains = [round(x, 2) for x in np.linspace(1, 10, 50+1)]
        proba_gains = [random.uniform(0.5, 1) for _ in gains]
        proba_gains = [p/sum(proba_gains) for p in proba_gains]

        gain_selectionne = random.choices(gains, weights=proba_gains, k=1)[0]

    else: # == "Hausse significative":
        #hausse significative de 10% à 20%
        gains = [round(x, 2) for x in np.linspace(10, 20, 100+1)]
        proba_gains = [random.uniform(0.5, 1) for _ in gains]
        proba_gains = [p/sum(proba_gains) for p in proba_gains]

        gain_selectionne = random.choices(gains, weights=proba_gains, k=1)[0]

    nouvelle_valeur = ancienne_valeur * (1 + gain_selectionne / 100.0)
    return nouvelle_valeur