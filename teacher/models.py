from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30,null=False, blank= False)
    address = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    website = models.URLField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.PositiveBigIntegerField()
    date_joined = models.DateTimeField()
    
    
    def __str__(self):
        return self.name
    
    