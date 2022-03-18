from pyexpat import model
from statistics import mode
from datetime import time
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}, {self.job_role}"


class Skills(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    current_level = models.IntegerField(default=1)
    required_level = models.IntegerField(default=1)
    last_updated = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} is level {self.current_level} at {self.subject}, the required level is a {self.required_level}, this was last updated on {self.last_updated}"

    def get_user_name(self):
        return self.user.name

    def get_subject_name(self):
        return self.subject.name