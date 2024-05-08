from django.db import models

# Create your models here.

class Category_model(models.Model):

    category_name= models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.category_name

class Employee_model(models.Model):

    employee_name=models.CharField(max_length=100,null=False)
    employee_place=models.CharField(max_length=100,null=False)
    employee_mobile_number=models.CharField(max_length=12,null=False)    
    employee_category=models.ForeignKey(Category_model,on_delete=models.CASCADE)

    