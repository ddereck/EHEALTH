from django.db import models

class Report(models.Model):
    # Champs pour stocker les informations du rapport
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
