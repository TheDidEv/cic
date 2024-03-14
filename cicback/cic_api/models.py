from django.db import models

class ArrayModel(models.Model):
    Id = models.AutoField(primary_key=True)
    Value = models.IntegerField()
    
    def __str__(self):
        return self.task
