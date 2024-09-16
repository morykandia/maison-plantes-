from rest_framework import serializers
from category.serializers import  CategorySerializers
from product.models import Produit

#
class ProductSerializer(serializers.ModelSerializer):
    categorie = CategorySerializers()
    class  Meta:
        model = Produit
        fields = ["id", "categorie","name" ,  "price" , "digital",  "image", "date_ajout"]