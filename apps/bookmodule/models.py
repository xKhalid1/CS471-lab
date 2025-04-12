from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 50) 
    author = models.CharField(max_length = 50) 
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1, null = False)


class Address(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.age}) - {self.address.city}"