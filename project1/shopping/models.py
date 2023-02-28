from django.db import models

class Product(models.Model):
    category=models.CharField(max_length=150,null=False,blank=False)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    small_description=models.TextField(max_length=250,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)

    def __str__(self):
        return self.name
