from django.db import models

class Note(models.Model):
    """
        Model for storing notes
    """
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title
