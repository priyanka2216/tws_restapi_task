from django.db import  models



class Category(models.Model):
    name = models.CharField(max_length=20)
 #  *************we use decorator(@) static mathod********
    @staticmethod
    def get_all_categories():
         return Category.objects.all()

    def __str__(self):
        return self.name

# def __str__(self): ka use krte hai category main kuch bhi value return kra skte ho


