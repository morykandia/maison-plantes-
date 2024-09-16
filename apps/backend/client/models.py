from django.db import models
from users.models import UserAccount

class Client(models.Model):
    user = models.OneToOneField(UserAccount, null=True, blank=True, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name 
