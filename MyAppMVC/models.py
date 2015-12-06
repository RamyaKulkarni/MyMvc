from django.db import models
from django.contrib import admin


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pub_date = models.DateField()
    hero_image = models.ImageField(upload_to="/images/" , blank = True)
    category = models.CharField(max_length=50)
    body_text = models.TextField()

admin.site.register(Article)
    

