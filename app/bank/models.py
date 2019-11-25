from django.db import models
import uuid



# Create your models here.

class Branch(models.Model):
    bank_name = models.CharField(max_length=200)
    bank_location = models.CharField(max_length=200)
    location_id = str(uuid.uuid4())
    def __str__(self):
        return (f"Bank Name: {self.bank_name} | {self.location_id}")

class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )

    customer_first_name = models.CharField(max_length=200)
    customer_last_name = models.CharField(max_length=200)
    customer_email = models.EmailField(unique=True, null=False, blank=False)
    
    def __str__(self):
        return (f"Name: {self.customer_first_name} {self.customer_last_name} | Bank: {self.branch.bank_name}")

class Product(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE
    )
    product_options = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('debit', 'DEBIT'),
        ('credit', 'CREDIT')
    )
    product_options = models.CharField(
        max_length=200,
        choices = product_options,
        default = product_options[0]
    )
    def __str__(self):
        return (f"Customer Name: {self.customer.customer_first_name}")