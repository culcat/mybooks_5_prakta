from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='covers/')
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/')