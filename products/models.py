from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 20)
    url = models.URLField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=1)
    #This will store the unique id of every user voting for our product
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)


    def summary(self):
        return self.body[:300]
        
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    #Name that is displayed in admin panel
    def __str__(self):
        return self.title



