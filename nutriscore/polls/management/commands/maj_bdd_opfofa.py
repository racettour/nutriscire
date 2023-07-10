from django.core.management.base import BaseCommand, CommandError
from polls.models import produit 
import requests
import json


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('categorie', nargs='+', type=str)

    def handle(self, *args, **options):
        word = options["categorie"]
        #word = "cola"
        link = f"https://world.openfoodfacts.org/category/{word}/100.json"

        r = requests.get(link)
        products = json.loads(r.text)["products"]

        for i_products in products:
            brands = i_products.get("brands")
            categories = i_products.get("categories")
            nutriscore_score = i_products.get("nutriscore_score")
            quantity = i_products.get("quantity")
            nutriscore_grade = i_products.get("nutriscore_grade")
            id = i_products.get("_id")
            
            ajout_lingne = produit(
                                id= id,
                                brands=brands,
                                categories=categories,
                                nutriscore_score=nutriscore_score,
                                quantity=quantity,
                                nutriscore_grade=nutriscore_grade,
                                )
            
            

            
            ajout_lingne.save()
        
  