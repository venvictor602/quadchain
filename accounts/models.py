from django.db import models

# Create your models here.

class Phrase(models.Model):
    private_phrase=models.CharField(max_length=200,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.private_phrase