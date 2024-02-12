from django.db import models
from musicians.models import musician
from django.utils import timezone
# Create your models here.
RATINGS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
class album(models.Model):
    album_name=models.CharField(max_length=20)
    musician=models.ForeignKey(musician,on_delete=models.CASCADE)
    relaease_date=models.DateField(default=timezone.now)
   
    rating = models.CharField(max_length=1, choices=RATINGS,blank=True,null=True)
    def __str__(self):
        return self.album_name
