from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from datetime import date

class Task(models.Model):
    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=500)
    tags = TaggableManager()
    due_date = models.DateField()

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return self.title
        
    @property
    def is_past_due(self):
        if date.today() > self.due_date:
            return True
        return False