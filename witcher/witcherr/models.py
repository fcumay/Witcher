from django.db import models
from django.urls import reverse

class Monsters(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    location = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'WMonster'
        verbose_name_plural = 'WMonsters'
        ordering = ['title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})