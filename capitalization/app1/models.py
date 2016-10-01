from django.db import models

# Create your models here.


class moDEl1(models.Model):
    pass

class Model2(models.Model):
    fk_to_model1 = models.ForeignKey(moDEl1)
