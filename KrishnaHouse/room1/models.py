from django.db import models

# Create your models here.

class BioData(models.Model):
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    State = models.CharField(max_length = 30)
    City = models.CharField(max_length = 30)
    About = models.TextField(blank = True)
    DOB = models.DateField(null = True)
    def __str__(self):
        return self.Name
