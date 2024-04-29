from django.db import models
from django.utils.translation import gettext_lazy as _

from boards.models import Board
from core.models import BaseModel

class Task(BaseModel):
    class Status(models.TextChoices):
        PROGRESS = 'progress', _('In Progress')
        DONE = 'done', _('Done')
        CANCELLED = 'cancelled', _('Won\'t do')
    
    class Icons(models.TextChoices):
        WORK = 'work', _('Technologist')
        SPEECH = 'speech', _('SpeechBalloon')
        COFFEE = 'coffee', _('HotBeverage')
        WEIGHTLIFTER = 'weightlifter', _('Weightlifter')
        BOOKS = 'books', _('Books')
        CLOCK = 'clock', _('ClockAlarm')

        
        
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=25,choices=Icons.choices, null=True)
    status = models.CharField(max_length=25, choices=Status.choices, null=True)
    board= models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')