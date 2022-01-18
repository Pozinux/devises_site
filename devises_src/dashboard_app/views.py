from django.shortcuts import render, redirect

import api


def redirect_index(request):
    # On veut rediriger vers home en lui passant des valeurs par défaut
    return redirect("home", days_range=365, currencies="USD,CAD")


# Create your views here.
def dashboard(request, days_range=60, currencies="CAD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    return render(request, "dashboard_app_templates/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "currencies": currencies,
                                                         "page_label": page_label})