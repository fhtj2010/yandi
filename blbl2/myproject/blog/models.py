from django.db import models
from django.contrib.auth.models import User
#
# 错误集合
from django.db.models.fields import exceptions
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name="博客类型")

    class Meta:
        verbose_name = verbose_name_plural = "博客类型"

    def __str__(self):
        return self.type_name

    objects = models.Manager()


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    title = models.CharField(max_length=50, verbose_name="标题")
    content = RichTextUploadingField(verbose_name="内容")
    # readed_num = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name="所属博客类型")

    # 返回值
    def get_read_num(self):
        try:
            return self.readnum.read_num

        # 对象不存在
        except exceptions.ObjectDoesNotExist :
            return 0

    class Meta:
        verbose_name = verbose_name_plural = "博客信息"
        ordering = ("-created_time",)

    def __str__(self):
        return self.title

    objects = models.Manager()


class ReadNum(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING, verbose_name="阅读所属文章")
    read_num = models.IntegerField(default=0, verbose_name="阅读次数")

    class Meta:
        verbose_name = verbose_name_plural = "阅读次数"



    objects = models.Manager()
