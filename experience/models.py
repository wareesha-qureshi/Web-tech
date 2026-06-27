from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.role} at {self.company}"
