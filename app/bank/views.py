from bank.models import Branch, Customer, Product
from rest_framework import viewsets
from bank.serializers import Branch_Serializer, Customer_Serializer, Product_Serializer

# from bank.models import Branch, Customer, Product
# from rest_framework import viewsets
# from bank.serializers import Branch_Serializer, Customer_Serializer, Product_Serializer


class Branch_Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows branch to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = Branch_Serializer

class Customer_Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows customer to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer

class Product_Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = Product_Serializer