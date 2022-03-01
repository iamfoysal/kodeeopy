from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

