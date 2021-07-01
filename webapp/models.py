from django.db import models

# Create your models here.
class employees(models.Model):
    emp_id=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
