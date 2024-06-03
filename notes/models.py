from django.db import models

class Note(models.Model):
    content = models.TextField()

    def __str__(self) -> str:
        return f'{' '.join(self.content.split()[:3])}...'

