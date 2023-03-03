from django.db import models

# Create your models here.

class Task(models.Model):
        title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Title")
        date = models.CharField(max_length=100, null=False, blank=False, verbose_name="Date")
        description = models.TextField(max_length=200, null=False, blank=False, verbose_name="Description")
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
        updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
        type = models.ManyToManyField(to='webapp.Type', related_name='task', blank=True)
        status = models.ManyToManyField(to='webapp.Status', related_name='task', blank=True)

        def __str__(self):
            return self.title
