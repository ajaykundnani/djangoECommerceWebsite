from django.db import models

# Create your models here.

class Product(models.Model):
    p_name = models.CharField(max_length=10)
    p_price = models.IntegerField(default=5000)
    p_desc = models.CharField(max_length=20)
    p_img = models.ImageField(null=True,blank=True,upload_to='pics/')

    @staticmethod
    def getProductsByIds(ids):
        return Product.objects.filter(id__in = ids)


class Users(models.Model):
    u_name = models.CharField(max_length=20)
    u_pass = models.CharField(max_length=20)
    u_email = models.EmailField()

    def __str__(self):
        return self.u_name
