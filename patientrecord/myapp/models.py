from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def abc(self):
        time_difference = relativedelta(datetime.today(), self.date_of_birth)
        years = time_difference.years
        if years == 0:
            return self.date_of_birth
        else:
            return years
    age = property(abc)


class PatientCureHistory(models.Model):
    disease = models.CharField(max_length=50)
    cure = models.TextField()
    cure_date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    def abc(self):
        time_difference = relativedelta(self.cure_date, self.patient.date_of_birth)
        years = time_difference.years
        return years
    age = property(abc)



# Create your models here.
