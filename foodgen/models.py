from django.db import models

# Create your models here.

class Gen(models.Model):
    name = models.CharField(max_length=30)
    utype = models.CharField(max_length=30)
    price = models.BooleanField(default=True)

    def __unicode__(self):
        return "{} - {} - Less than $10: {}".format(self.name,self.utype,self.price)