from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)
    location = models.FloatField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s" % self.name


class Academican(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
