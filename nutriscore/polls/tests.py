from django.test import TestCase
import requests
import json
from .models import produit
from django.shortcuts import render,get_object_or_404



def add_product(  id,brands,categories,nutriscore_score, quantity,
            nutriscore_grade):
    
             
        product_select = produit.objects.create(
            id= id,
            brands=brands,
            categories=categories,
            nutriscore_score= nutriscore_score,
            quantity=quantity,
            nutriscore_grade=nutriscore_grade
        )
        
        
  
        
        
        return product_select
    
        

# Create your tests here.

class produit_varaible_typeTests(TestCase):
    def test_id_type(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        
        
        product_select = add_product(1,"brands","categories",20, "quantity",
            "nutriscore_grade")
        product = get_object_or_404(produit, pk=1)

        self.assertIs(type(product.brands)==str   , True)
        self.assertIs(type(product.categories)==str   , True)
        self.assertIs(type(product.nutriscore_score)==int   , True)
        self.assertIs(type(product.quantity)==str   , True)
        self.assertIs(type(product.nutriscore_grade)==str   , True)
        
    def test_blank_value(self):
        product_select = add_product(1,None,"categories",20, "quantity",
            "nutriscore_grade")
        product = get_object_or_404(produit, pk=1)
        
        self.assertIs(product.brands  , "")
        
        
        
        
        
        
