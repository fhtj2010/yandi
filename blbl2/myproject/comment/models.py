from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name="关联的类型")
    object_id = models.PositiveIntegerField(verbose_name="关联的id")
    content_object = GenericForeignKey("content_type", "object_id")

    text = models.TextField(verbose_name="评论内容")
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING, verbose_name="评论者")
    # parent_id = models.IntegerField(default=0)

    root = models.ForeignKey("self", related_name="root_comment", null=True, on_delete=models.DO_NOTHING,
                             verbose_name="顶级")
    parent = models.ForeignKey("self", related_name="parent_comment", null=True, on_delete=models.DO_NOTHING)
    reply_to = models.ForeignKey(User, related_name="replies", null=True, on_delete=models.DO_NOTHING,
                                 verbose_name="回复谁")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = verbose_name_plural = "评论信息"
        ordering = ['comment_time']

    objects = models.Manager()
