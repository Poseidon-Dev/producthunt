from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    title = models.TextField(max_length=255)
    url = models.URLField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_concat(self):
        return self.pub_date.strftime('%B %e, %Y')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
