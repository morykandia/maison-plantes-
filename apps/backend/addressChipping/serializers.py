from rest_framework  import serializers
from client.serializers import ClientSerializers
from command.serializers import CommandSerializers
from addressChipping.models import AddressChipping


class AdressChippingSerializer(serializers.ModelSerializer):
    client = ClientSerializers()
    commande = CommandSerializers()
    class Meta:
        model = AddressChipping
        fields = [" client","commande", "addresse", "ville", "zipcode", "date_ajout" ]