from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=250, blank=True, null=False)
    date_created = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.post
    