from django.http import HttpResponse
from django.shortcuts import render, redirect

import api


# Par convention, on appelle le paramètre "request" qui est la requête faite par l'utilisateur. 
# Pour pouvoir récupérer des informations comme par exemple dans l'url, d'un formulaire si on a une requête de type POST etc.

# redirect permet de rediriger l'utilisateur
def redirect_index(request):
    return redirect("home", days_range=365, currencies="USD,CAD")


# Create your views here.

# render permet de retourner un template

def dashboard(request, days_range=60, currencies="CAD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "currencies": currencies,
                                                         "page_label": page_label})


def fonctionDeTest(request):
    # return HttpResponse("Coucou !")
    # context permet de passer des variables par un dictionnaire
    return render(request, "dashboard_app/index.html", context={"var1": "Regarde ! Je sais compter", "liste_nombres": range(10)})
