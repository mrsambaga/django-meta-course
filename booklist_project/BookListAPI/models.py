from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.title

    class Meta():
        indexes = models.Index(fields=['price']),
