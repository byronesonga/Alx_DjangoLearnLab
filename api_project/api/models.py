from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)   # book title
    author = models.CharField(max_length=100)  # book author

    def __str__(self):
        return self.title



