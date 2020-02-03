from django.contrib import admin

# Register your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, defualt='')
    description = models.TextField()
    price = models.DecimalField()
