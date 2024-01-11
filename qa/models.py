from django.db import models

# Create your models here.

class User(models.Model):
    # First_name Last_name Email Password 
    frist_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,blank = True)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=20,blank = False)



    # class Post():
        # posted_by posted_content create_at comments

    # class Comments():
        # commented_by commented_at post 
    


class Books(models.Model):
    title = models.CharField(max_length=100)
    total_pages = models.IntegerField()
    author_name = models.CharField(max_length=100)
