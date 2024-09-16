from django.contrib import admin
from product.models import Produit

@admin.register(Produit)
class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        "categorie",
        "name",
        "price",
        "digital",
        "image",
        "date_ajout"

    )
