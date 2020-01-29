from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户名")
    nickname = models.CharField(max_length=20, verbose_name="昵称")

    def __str__(self):
        return '<Profile: %s for %s >' % (self.nickname, self.user.username)

    class Meta:
        verbose_name = verbose_name_plural = "用户信息"

    objects = models.Manager()


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''

def has_nickname(self):
    return Profile.objects.filter(user=self).exists()


User.get_nickname = get_nickname
User.has_nickname = has_nickname
