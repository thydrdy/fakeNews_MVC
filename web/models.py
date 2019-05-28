from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(help_text="Please Input a valid Email address")
    password=models.CharField(max_length=200)


class News(models.Model):
    news_link=models.TextField()
    thread_name=models.CharField(max_length=200)
    head_line=models.CharField(max_length=200)
    by=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    additional_text=models.TextField()
    img_path=models.ImageField(upload_to="images/",blank=True)
    date_created=models.DateTimeField('date created',blank=True)
    down_val=models.BigIntegerField(default=0)
    up_val=models.BigIntegerField(default=0)

class Search(models.Model):
    news_link=models.CharField(max_length=200,blank=True)
    thread_link=models.CharField(max_length=200,blank=True)
    status=models.BooleanField(blank=False)

