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
    

class Card(models.Model):
    card_number = models.IntegerField()


class Departement(models.Model):
    name = models.CharField(max_length=50)

class Course(models.Model):
    title = models.CharField(max_length=20)
    code = models.IntegerField()


class Student9(models.Model):
    name = models.CharField(max_length=50)
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    Courses = models.ManyToManyField(Course)
