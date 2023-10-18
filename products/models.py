from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
                                
    datatime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
    
    

class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
         
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments') # product.comments for getting all the comments of this product
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments') # when we want to know all the comments of 
                                                        # a specific author, we can use user.comments (comments is because of related_name)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) # it meand by default comments are approved 
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    