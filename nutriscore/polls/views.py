
from django.http import HttpResponse,HttpResponseRedirect
from .models import produit
from django.shortcuts import render,get_object_or_404
from django.urls import reverse









def index(request):
    best_nutriscore = produit.objects.all()
    #best_nutriscore = produit.objects.get(id="12000002489")
    context = {"best_nutriscore": best_nutriscore}
    return render(request, "polls/index.html", context)


def detail(request, id):
    product = produit.objects.get(id=id)
    
    product = get_object_or_404(produit, pk=id)

    
    context = {  
               "produit" : produit.objects.filter(
                    nutriscore_score__lt = product.nutriscore_score
                    ),
               "product" : product,}
    return render(request, 'polls/id_infos.html', context)


def vote(request, product_id):
    pk_ind= request.POST['choice']
    
    question = get_object_or_404(produit, pk=pk_ind)
        
    #list_prod = produit.objects.filter(nutriscore_score__gte =12)
 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results',
                                    args=(pk_ind,)))
    
        

def results(request, pk_ind):
    pk_ind= request.POST['choice']
    product = get_object_or_404(produit, pk=pk_ind)
    context = {  
              "produit" : produit.objects.all(),
              "product" : product,}
     
    return render(request, 'polls/results.html', context)

