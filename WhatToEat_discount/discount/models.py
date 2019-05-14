from django.db import models


class Discount(models.Model):
    Store = models.CharField(primary_key=True , max_length=200)
    Discount_Number = models.CharField(max_length=200)
    Deadline = models.CharField(max_length=50)
    Notice = models.CharField(max_length=200)

    def __str__(self):
        return self.Store