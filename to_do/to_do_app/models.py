from django.db import models


class Task(models.Model):
    """Model to database"""
    text: str = models.CharField('text', max_length=200)

    def __repr__(self) -> str:
        return str(self.text)
