from django.db import models
from datetime import datetime

# Create your models here.
class ProductList(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField(default=0)
    rating=models.IntegerField(default=0)
    created_at=models.DateTimeField(default=datetime.now())
    

    def __str__(self):
        return self.title
    
    