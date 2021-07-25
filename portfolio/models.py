from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.db.models.query_utils import DeferredAttribute


class Portfolio(models.Model):
    TYPE_CHOICES = [('web', 'Web'), ('app', 'App')]
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique_with='updated__month')
    image = models.ImageField(upload_to='portfolio-images')
    port_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='web')
    description = models.TextField()
    live_url = models.URLField(null=True, blank=True)
    source_url = models.URLField(null=True, blank=True)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Screenshot(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio-screenshots')

    def __str__(self):
        return "<Screenshot <{}>>".format(str(self.portfolio))
