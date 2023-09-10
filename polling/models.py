from django.db import models


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=128)
    test = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
