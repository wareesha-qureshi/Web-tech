from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name
