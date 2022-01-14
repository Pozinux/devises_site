from datetime import date, timedelta
from pprint import pprint

import requests


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    
    # requete = f"https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&symbols={symbols}"
    # L'API de exchangeratesapi.io n'étant plus disponible, j'utilise à la place exchangerate.host
    requete = f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}"

    # la méthode get permet de faire un requête http de type GET
    r = requests.get(requete)

    # on pourrait vérifier si la requête a réussi (return code status 200) 
    # mais on peut aussi vérifier si la requête a échoué (on se fiche du code de retour)
    # et on vérifie que les données retournée sont au format json.
    # Les gens de l'api pourraient décider de retourner du xml par ex. 
    # La requête serait donc ok qd même mais notre api ne marcherait pas puisque l'on attend du JSON.
    # L'ordre du "and" est donc important
    if not r and not r.json():
        return False, False

    api_rates = r.json().get("rates")
    
    # Pour tester 
    # pprint(api_rates)
    # return None, None 

    # Création d'une compréhension de dictionnaire
    # On va boucler sur les devises et pour chaque devis on va créer une paire de clé (currency:). La clé va être la devise et la valeur une liste vide
    # La liste vide va être remplie par la suite à l'intérieur de la boucle for plus loin
    all_rates = {currency: [] for currency in currencies}
    # Pour tester 
    # pprint(all_rates)
    all_days = sorted(api_rates.keys())

    # Boucle à travers le dictionnaire qui contient la devise et ses valeurs
    for each_day in all_days:
        # Compréhension de liste pour tous les éléments, on boucle sur la devise et ses valeurs et on les ajoute à la liste
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    # Pour tester, on a bien un dictionnaire avec la devise en clé et la liste de toutes les valeurs de la devise en valeurs 
    # pprint(all_rates)

    return all_days, all_rates


# Pour éviter que le code de test soit exécuté lorsque l'on va importer l'API dans l'interface Django
if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])
    # Debug
    # On a bien la liste des jours et ensuite le dictionnaire avec les devises et la liste de leurs valeurs
    # pprint(days)
    # pprint(rates)