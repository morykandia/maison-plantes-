from django.db import models
from category.models import Category
from django.utils import timezone

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Produit(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, default='posts/default.jpg')
    date_ajout = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.name 

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url             
