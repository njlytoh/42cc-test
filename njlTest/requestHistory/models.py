from django.db import models

# Create your models here.

class RequestsHistory(models.Model):

    url = models.CharField("Http request url", max_length=255)
    post_options = models.TextField()
    get_options = models.TextField()

