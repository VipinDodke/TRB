from django.db import models

# Create your models here.
class page(models.Model):
    blog_id= models.AutoField
    blog_name=models.CharField(max_length=200,default='')
    desc=models.CharField(max_length=700,default='')
    desc1=models.CharField(max_length=700,default='')
    post_date=models.DateField()
    TypeBlog=models.IntegerField(default=0)
    image=models.ImageField(upload_to="blog/images",default="")
    video=models.FileField(upload_to="blog/video",default='')
    def __str__(self):
        return self.blog_name


class Contect(models.Model):
    msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,default='')
    Call = models.IntegerField()
    desc = models.CharField(max_length=1100)
    def __str__(self) :
        return self.Name