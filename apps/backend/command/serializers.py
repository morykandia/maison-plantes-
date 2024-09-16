from rest_framework import serializers
from client.serializers import ClientSerializers
from command.models import Commande

class CommandSerializers(serializers.ModelSerializer):
    
    client = ClientSerializers()
    class Meta:
        model = Commande
        fields = ["client", "date_commande", "complete", "transaction_id", " status", "total_trans"]

