from django.db import models


# Create your models here.
class Task(models.Model):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    STATUS_CHOICES = [(TODO, "TO DO"), (IN_PROGRESS, "IN PROGRESS"), (DONE, "DONE")]

    task_description = models.TextField()
    task_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=TODO)
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_description
