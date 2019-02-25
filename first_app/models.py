from django.db import models


# Create your models here.

class RealUser(models.Model):
    email_id = models.CharField(max_length=36)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)

    def __str__(self):
        return self.email_id
