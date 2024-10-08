from rest_framework import serializers
from category.models import Category


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description',"image"]