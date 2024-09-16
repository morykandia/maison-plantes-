from rest_framework import serializers
from command.serializers import CommandSerializers
from product.serializers import ProductSerializer
from commandArticle.models import CommandeArticle

class CommandArticleSerializer(serializers.ModelSerializer):
     produit = ProductSerializer()
     commande = CommandSerializers()
     class Meta:
        model = CommandeArticle
        fields = ["produit", "commande", " quantite", "date_added"]