from django.db import models
from uuid import uuid4
from rest_framework import serializers
# Create your models here.


def upload_image_book(instance,filename):
    return f"{instance.id}-{filename}"

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=upload_image_book, blank=True, null=True)

class Articles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=1000)
    firstParagraph = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
   
    def clean(self):
        if self.body is not None:
            if len(self.body) < 50:
                raise serializers.ValidationError({"body": 'body minimum digits is 50'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

   





  
   
   
    
   