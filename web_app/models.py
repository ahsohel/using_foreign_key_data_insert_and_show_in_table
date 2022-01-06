from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.roll


class result(models.Model):
    student_info = models.ForeignKey(student, on_delete=models.CASCADE)
    Status = models.CharField(max_length=20)
