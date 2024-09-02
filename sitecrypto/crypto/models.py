from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Crypto.Status.PUBLISHED)


class Crypto(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    title = models.CharField(max_length=50, db_index=True)
    full_name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    networks = models.ManyToManyField(
        'Network',
        related_name='networks',
    )
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        unique_together = ('title', 'slug', 'full_name')
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Network(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    full_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('network', kwargs={'net_slug': self.slug})
