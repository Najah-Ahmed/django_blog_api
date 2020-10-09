from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return self.title
