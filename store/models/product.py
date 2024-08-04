from django.db import models
from .category import Category
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products')
    date_added = models.DateTimeField(default=timezone.now) 


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
           return Product.objects.filter(category= category_id)
        else:
            return Product.get_all_products()







''' 
   @staticmethod
    def get_all_products_by_categoryid(category_id):
        #if lga hai agar id lgi hai toh vo hi product show krna jiski id lgi hai
        if category_id: 
            return Product.objects.filter(category = category_id) 
        #else means id nhi lgi toh sare product show hoga
        else:
            return Product.get_all_products()


'''





