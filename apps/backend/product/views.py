from rest_framework.views import APIView
from rest_framework.response import Response
from  product.models import Produit
from product.serializers import ProductSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser



class ProductsViewsAll(APIView):
    def get(self, *args, **kwargs):
        products = Produit.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    


class ProductsViewsId(APIView):
    def get_object(self, pk):
        try:
            return Produit.objects.get(pk=pk)
        except Produit.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    
class ProductsViewsPost(APIView):
    def post(self, request, format=None):
        parser_classes = [MultiPartParser, FormParser]
        serializer = ProductSerializer(data=request.data)
        if request.user.is_authenticated and request.user.is_superuser:
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsViewsUpdate(APIView):     
    def get_object(self, pk):
        try:
            return Produit.objects.get(pk=pk)
        except Produit.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductSerializer(products, data=request.data)
        if request.user.is_authenticated and request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductsViewsDeleted(APIView):
    def get_object(self, pk):
        try:
            return Produit.objects.get(pk=pk)
        except Produit.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        products = self.get_object(pk)
        if request.user.is_authenticated and request.user.is_superuser:
            products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
