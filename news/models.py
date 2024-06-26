from django.db import models

# Create your models here.

class journalist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Article(models.Model):
    author = models.ForeignKey(journalist, on_delete=models.CASCADE, related_name='articles')
    # author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    body = models.TextField()
    location = models.CharField(max_length=255)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} {self.title}"
