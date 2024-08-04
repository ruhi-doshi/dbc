from django.db import models


class RaiseTicket(models.Model):
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    #image = models.ImageField(upload_to='images/')
    class Meta:
        db_table="raisingticket"



