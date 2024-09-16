from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from users.serializers import*
from django.http import Http404
#from custom_commands.permissions import  IsAdminAuthenticated

class RegisterView(APIView):
    def post(self, request):
      data = request.data

      serializer = UserCreateSerializer(data=data)

      if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      user = serializer.create(serializer.validated_data)
      user =UserAcountSerializer(user)
      return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user = UserAcountSerializer(user)
        return Response(user.data, status=status.HTTP_200_OK)
    

class UserAccountAPIView(APIView):
    #permission_classes = [IsAdminAuthenticated]
    def get(self, *args, **kwargs):
        allUsers = UserAccount.objects.all()
        serializer = UserAcountSerializer(allUsers, many=True)
        return Response(serializer.data)

class UserAcccountAPIViewUpdateOrDelete(APIView):
    #permission_classes = [IsAdminAuthenticated]
    def get_object(self, pk):
        try:
            return UserAccount.objects.get(pk=pk)
        except UserAccount.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserAcountSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserAcountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

