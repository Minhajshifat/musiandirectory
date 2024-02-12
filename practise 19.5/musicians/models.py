from django.db import models

# Create your models here.
class musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=40)
    Email=models.EmailField(max_length=100)
    Phone_number=models.CharField(max_length=11)
    instruments=[('Piano','Piano'),('Mridangam','Mridangam'),('Flute','Flute'),('Violin','Violin')]
    instrument_type=models.CharField(max_length=10,choices=instruments)

    def __str__(self):
        return self.first_name