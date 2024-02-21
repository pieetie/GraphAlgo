import random
import numpy as np

def baisse(ancienne_valeur):
    """
    dépend largement des conditions de marché et de l'entreprise
    probabilités à changer en fonction du type d'action...
    (à compléter)
    """
    probabilite_faillite = 0.001 
    probabilite_chute = 0.005
    probabilite_baisse = 1 - probabilite_faillite - probabilite_chute

    options = ["Faillite", "Baisse", "Chute"]
    probabilites = [probabilite_faillite, probabilite_baisse, probabilite_chute]

    selection = random.choices(options, weights=probabilites, k=1)[0]

    if selection == "Faillite":
        #pertes pour une faillite de 10% à 95% 
        pertes = [round(-x, 2) for x in np.linspace(10, 95, 85*10+1)]
        proba_pertes = [random.uniform(0.5, 1) for _ in pertes]
        proba_pertes = [p/sum(proba_pertes) for p in proba_pertes]
        
        perte_selectionnee = random.choices(pertes, weights=proba_pertes, k=1)[0]
    
    elif selection == "Chute":
        #pertes pour une chute de 5% à 10%
        pertes = [round(-x, 2) for x in np.linspace(5, 10, 50+1)]
        proba_pertes = [random.uniform(0.5, 1) for _ in pertes]
        proba_pertes = [p/sum(proba_pertes) for p in proba_pertes]
        
        perte_selectionnee = random.choices(pertes, weights=proba_pertes, k=1)[0]

    else: # == "Baisse":
        #pertes pour une baisse de 0.01% à 1%
        pertes = [round(-x, 2) for x in np.linspace(0.01, 1, 499+1)]
        proba_pertes = [random.uniform(0.5, 1) for _ in pertes]
        proba_pertes = [p/sum(proba_pertes) for p in proba_pertes]
        
        perte_selectionnee = random.choices(pertes, weights=proba_pertes, k=1)[0]
        
    nouvelle_valeur = ancienne_valeur * (1 + perte_selectionnee / 100.0)
    return nouvelle_valeur