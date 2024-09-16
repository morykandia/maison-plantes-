from django.db import models
from client.models import Client

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True) 
    status = models.CharField(max_length=200, null=True, blank=True)
    total_trans = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)  

    @property
    def produit_physique(self):
        """ savoir si nous avons au moins un produit physique"""
        articlecommande = self.commandearticle_set.all()
        physique = any(article.produit.digital==False for article in articlecommande)
        return physique
    
    @property 
    def get_panier_total(self):
        """ prix total des articles dans le panier"""
        articlecommande = self.commandearticle_set.all()
        total = sum([article.get_total for article in articlecommande])
        return total  

    @property
    def get_panier_article(self):
        """ Nombre total des articles dans le panier"""
        articlecommande = self.commandearticle_set.all()
        quantite_total = sum([article.quantite for article in articlecommande])
        return quantite_total
