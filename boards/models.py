from django.db import models

from core.models import BaseModel


class Board(BaseModel):
    """
    Represents a board in the application, which can contain tasks.
    """

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.title, self.created_at)



