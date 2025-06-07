from django.db import models
from django.contrib.auth.models import User

class Book (models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=30)
    description=models.TextField()
    publication_date=models.DateField()


    def __str__(self):
        return self.title


class Review(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    review_author=models.CharField(max_length=1000)
    review=models.TextField(null=True, blank=True)
    rating=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
    related_name="reviews")

    def __str__(self):
        return f"{self.review_author} - {self.rating}"
