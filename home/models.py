from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=30, null=True, blank= True)
    phone = models.PositiveBigIntegerField()
    
    
    def __str__(self):
        return self.name
    
    