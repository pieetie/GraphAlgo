import random
def tirage(probaNormale, proba_baisse, proba_hausse):
    """
    Permet de déterminer par le hasard si une hausse, une diminution 
    ou une distribution normale va s'appliquer
    """
    options = ["Baisse", "Normale", "Hausse"]
    probabilites = [proba_baisse, probaNormale, proba_hausse]

    selection = random.choices(options, weights=probabilites, k=1)[0]

    return selection