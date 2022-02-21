from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Point(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    day_of_week = models.CharField(max_length=30)
    #entrance
    #left

    def __str__(self):
        return self.employee, self.day_of_week, self.date
