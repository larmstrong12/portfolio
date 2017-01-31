from django.db import models

class Pricing(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    company = models.CharField(max_length=100)
    pages = models.CharField(max_length=10)
    requests = models.TextField()

    def __str__(self):
        return self.name

