from django.contrib import admin
from bank.models import Branch, Customer, Product

# Learn more or give us feedback
# from django.contrib import admin
# # from bank.models import views as bank_views
# from bank.models import Branch, Customer, Product

 # Register your models here.
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Product)


# # admin.site.register(Branch)
# admin.site.register(Customer)
# admin.site.register(Product)

# class Customer_Inline(admin.StackedInline):
#     model = Customer

# @admin.register(Branch)
# class Branch_Admin(admin.ModelAdmin):
#     inlines = [
#         Customer_Inline
#     ]