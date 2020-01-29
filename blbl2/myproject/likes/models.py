from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


# Create your models here.

class LikesCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    like_num = models.IntegerField(default=0, verbose_name="点赞数量")

    class Meta:
        verbose_name = verbose_name_plural = "点赞数量"

    objects = models.Manager()


class LikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "点赞记录信息"

    objects = models.Manager()
