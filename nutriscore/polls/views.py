
from django.http import HttpResponse
from .models import produit
from django.shortcuts import render

def index(request):
    best_nutriscore = produit.objects.all()
    #best_nutriscore = produit.objects.get(id="12000002489")
    context = {"best_nutriscore": best_nutriscore}
    return render(request, "polls/index.html", context)


def detail(request, id):
    product = produit.objects.get(id=id)
    
    context = {"product_id": product.id,
               "brands" : product.brands,
               "nutriscore" : product.nutriscore_grade,
               "note" : product.nutriscore_score,               
               }
    return render(request, 'polls/id_infos.html', context)

