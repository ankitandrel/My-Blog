from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    category_choices = (
        ('Web_Design','Web_Design'),
        ('HTML','HTML'),
        ('Freebies','Freebies'),
        ('JavaScript','JavaScript'),
        ('CSS','CSS'),
        ('Tutorials','Tutorials'),
    )
    heading_image = models.ImageField(upload_to = 'media/post/', blank = True, default = 'default.jpg')
    heading = models.CharField(max_length=255)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    blog_category = models.CharField(max_length=155, choices=category_choices, default='....')


    def __str__(self):
        return self.heading