from django.db import models
from django.contrib.auth.models import models, User

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
    liked =models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    def __str__(self):
        return self.blog_name

    @property
    def num_like(self):
        return self.liked.all().count()

Like_CHOICES=(
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(page, on_delete=models.CASCADE)
    value = models.CharField(choices=Like_CHOICES, default='Like',max_length=10)

    def __str__(self):
        return str(self.post)


class Contect(models.Model):
    msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,default='')
    Call = models.IntegerField()
    desc = models.CharField(max_length=1100)
    def __str__(self) :
        return self.Name