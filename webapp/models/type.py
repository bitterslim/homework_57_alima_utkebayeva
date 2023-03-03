from django.db import models

class Type(models.Model):
    name = models.CharField(max_length= 50, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    def __str__(self):
        return self.name