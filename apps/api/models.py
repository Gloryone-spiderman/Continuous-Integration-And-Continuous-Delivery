from django.db import models

# Create your models here.
class Qestion(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Qestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)