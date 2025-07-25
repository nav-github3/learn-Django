from django.db import models
from django.utils import timezone

# Create your models here.
class chaiVarieties(models.Model):
    name  = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'), 
        ('GR', 'GINGER'), 
        ('KL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]

    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    
    
def __str__(self):
    return self.name