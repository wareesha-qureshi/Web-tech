from django.db import models


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.degree} - {self.institution}"
