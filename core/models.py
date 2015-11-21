from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from datetime import date

class Task(models.Model):
    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=500)
    tags = TaggableManager()
    due_date = models.DateField()
    is_complete = models.BooleanField(default=False)

    class Meta:
        '''
        Meta class to order taks.
        '''
        ordering = ['-due_date']

    def __str__(self):
        '''
        String method returning self.title.
        '''
        return self.title

    @property
    def is_past_due(self):
        '''
        Propety to check if the date is pastself.
        '''
        if date.today() > self.due_date:
            return True
        return False