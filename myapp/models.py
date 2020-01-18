from django.db import models


class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    batch = models.CharField(default=None, max_length=255)

    def __str__(self):
        return self.batch


class Student(models.Model):
    name = models.CharField(default=None,max_length=100)
    phone = models.CharField(default=None,max_length=10)
    email = models.CharField(default=None, max_length=255)
    batch = models.ForeignKey(Batch,default=None,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.phone + " " + self.email



