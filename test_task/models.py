from django.db import models


# Create your models here.

class Manufacturer(models.Model):
    create_manufacturer_date = models.DateTimeField(auto_now_add=True)
    manufacturer_name = models.CharField(max_length=100)


class Product(models.Model):
    create_product_date = models.DateTimeField(auto_now_add=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=100)


class Contract(models.Model):
    create_contract_date = models.DateTimeField(auto_now_add=True)
    description_contract = models.CharField(max_length=300, null=True)


class CreditApplication(models.Model):
    create_credit_date = models.DateTimeField(auto_now_add=True)
    description_application = models.CharField(max_length=300, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)  # related_name='applications'
