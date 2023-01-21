from django.db import models

class fdata(models.Model):
    food=models.CharField(max_length=255)
    quantity=models.IntegerField()
    calories=models.IntegerField()
    carbs = models.FloatField()
    protein=models.FloatField()
    fat=models.FloatField()

class rcal(models.Model):
    rcal=models.IntegerField(blank=True)

