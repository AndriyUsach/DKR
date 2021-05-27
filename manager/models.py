from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField()
    user = models.CharField(max_length=255)

    def __str__(self):
        return self.task.__str__()[:20]
    class Meta:
        unique_together = ('task', 'user', 'finish_date')
        ordering = ['user', 'finish_date']