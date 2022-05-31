import datetime
from random import randint

from django.db import models


class NewsModel(models.Model):
    name = models.CharField(max_length=80, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(
        blank=True,
        verbose_name="Image",
        upload_to=str(datetime.datetime.now()) + str(randint(-10000, 10000)),
    )
    tegs = models.ManyToManyField("TegsModel", related_name="tegs")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    views_new = models.IntegerField(verbose_name="Просмотры", default=0)

    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"
        ordering = ["-create_at"]

    def delete(self, *args, **kwargs):
        for i in self.additionalimage_set.all():
            i.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class AdditionalImage(models.Model):
    new = models.ForeignKey(NewsModel, on_delete=models.CASCADE, verbose_name="P")
    image = models.ImageField(
        upload_to=str(datetime.datetime.now()) + str(randint(-10000, 10000)),
        verbose_name="Image",
    )

    class Meta:
        verbose_name = "AddImage"


class TegsModel(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название тега", unique=True)

    class Meta:
        verbose_name = "Teg"

    def __str__(self):
        return self.name
