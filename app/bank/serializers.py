from rest_framework import serializers
from bank.models import Branch, Customer, Product

class Branch_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = [
            'bank_name',
            'bank_location'
        ]

class Customer_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'customer_first_name',
            'customer_last_name',
            'customer_email'
        ]

class Product_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_options'
        ]