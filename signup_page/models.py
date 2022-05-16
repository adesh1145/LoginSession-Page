
from django.db import models

# Create your models here.

class signup_detail(models.Model):
    fname=models.TextField(max_length=70)
    lname=models.TextField(max_length=70)
    img_name=models.FileField( upload_to='upload_adesh_files', max_length=100)
    uname=models.TextField(max_length=70)
    email_name=models.EmailField(max_length=254)
    pass1=models.TextField(max_length=70)
   
