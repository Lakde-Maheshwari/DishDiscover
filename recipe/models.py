from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q,UniqueConstraint

class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2000)
    desc = models.TextField(max_length=2000)
    ingredients = models.TextField(max_length=2000)  
    instructions = models.TextField(max_length=2000)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Use Cloudinary storage automatically
    recipe_img = models.ImageField(upload_to='images/')  

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=2000)
    date_posted = models.DateField(auto_now_add=True)
    recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

