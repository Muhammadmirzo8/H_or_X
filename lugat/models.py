from django.db import models

from django.db import models

class Soz(models.Model): 
    id = models.IntegerField(primary_key=True, unique=True)
    correct = models.CharField(max_length=20, unique=True) 
    def __str__(self):
        return f"{self.correct}" 


class nosoz(models.Model): 
    wrong = models.CharField(max_length=50)  
    soz_id = models.ForeignKey(Soz, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.wrong}"  

