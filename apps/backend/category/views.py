from rest_framework.views import APIView
from rest_framework.response import Response
from  category.models import Category
from category.serializers import CategorySerializers
from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CategoriesViewsAll(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class CategoriesViewsId(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    

class CategoryViewsPost(APIView):
    def post(self, request, format=None):
        parser_classes = [MultiPartParser, FormParser]
        serializer = CategorySerializers(data=request.data)
        if request.user.is_authenticated and request.user.is_superuser:
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewsUpdate(APIView):     
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializers(category, data=request.data)
        if request.user.is_authenticated and request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewsDeleted(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        if request.user.is_authenticated and request.user.is_superuser:
            category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


