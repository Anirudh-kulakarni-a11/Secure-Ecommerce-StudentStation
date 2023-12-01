import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)  # Use 'Book' directly
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(
        'Book',  # Use 'Book' directly
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse("book_detail")