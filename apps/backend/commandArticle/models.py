from django.db import models
from product.models import Produit
from command.models import Commande

class CommandeArticle(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantite * self.produit.price
        return total
