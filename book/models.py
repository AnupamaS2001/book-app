from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    genre=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
