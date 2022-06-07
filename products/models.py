from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return f"localhost:8000/api/v1/cat/{self.id}/"


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"localhost:8000/api/v1/products/{self.id}/"

    class Meta:
        ordering = ['-created_at']
