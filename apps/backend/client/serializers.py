from rest_framework import serializers
from client.models import Client
from users.serializers import UserAcountSerializer

class ClientSerializers(serializers.ModelSerializer):
    user = UserAcountSerializer()
    class Meta:
        model = Client
        fields = ["user", "name",  "email"]