from django.db import models


class Tweets(models.Model):
    name = models.CharField(max_length=250)
    tweet = models.CharField(max_length=50)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
