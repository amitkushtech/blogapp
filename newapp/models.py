from django.db import models

# Create your models here.
class BlogCategory(models.Model):
    BLOGCHOICE = (("Sports", "Sports"),)
    blog_name = models.CharField(max_length=50)
    blog_description = models.TextField()
    blog_choice = models.CharField(max_length=20, default="Sports", choices=BLOGCHOICE)

    def __str__(self):
        return self.blog_name
