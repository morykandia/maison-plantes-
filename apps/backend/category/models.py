from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, default='posts/default.jpg')

    def __str__(self):
        return self.name
