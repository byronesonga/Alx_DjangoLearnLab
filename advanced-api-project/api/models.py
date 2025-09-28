from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )  # Link to Author (one author -> many books)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"