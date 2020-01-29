from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django import template
from ..models import LikesCount, LikeRecord

register = template.Library()
@register.simple_tag
def get_likes_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    likes_count, created = LikesCount.objects.get_or_create(content_type=content_type, object_id=obj.pk)
    return likes_count.like_num

# takes_context=True这样使用相关模板变量
@register.simple_tag(takes_context=True)
def get_likes_status(context,obj):
    content_type = ContentType.objects.get_for_model(obj)
    user = context["user"]
    if not user.is_authenticated:
        return " "
    if LikeRecord.objects.filter(content_type=content_type, object_id=obj.pk, user=user).exists():
        return "active"

    else:
        pass

@register.simple_tag
def get_content_type(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return content_type.model
