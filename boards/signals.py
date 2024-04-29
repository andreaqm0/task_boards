from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Board
from tasks.models import Task


@receiver(post_save, sender=Board)
def create_default_tasks(sender, instance, created, **kwargs):
    if created:
        tasks = [
            {
                "name": "Task in Progress",
                "description": "",
                "icon": "clock",
                "status": "progress",
                "board": instance,
            },
            {
                "name": "Task Completed",
                "description": "",
                "icon": "weightlifter",
                "status": "done",
                "board": instance,
            },
            {
                "name": "Task Won't do",
                "description": "",
                "icon": "coffee",
                "status": "cancelled",
                "board": instance,
            },
            {
                "name": "Task To Do",
                "description": "Work on Challenge on devChallenges.io, learn TypeScript",
                "icon": "books",
                "status": None,
                "board": instance,
            },
        ]
        for task in tasks:
            Task.objects.create(**task)
