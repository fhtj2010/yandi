from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogType, Blog, ReadNum
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm
from account.forms import LoginForm
from django.http import JsonResponse

# 引入缓存
from django.core.cache import caches


# Create your views here.
def blog_list(request):
    all_blogs_list = Blog.objects.all()
    paginator = Paginator(all_blogs_list, 2)
    page_num = request.GET.get("page", 1)
    # get_page方法用于控制不是数字类型，默认返回页面1
    page_of_blogs = paginator.get_page(page_num)

    # 获取当前页
    current_page_num = page_of_blogs.number

    # 获取前后四页的范围
    page_range = list(range(max(current_page_num - 3, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 3, paginator.num_pages) + 1))

    # 加上省略标记
    if page_range[0] - 1 >= 4:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 4:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)

    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context["page_of_blogs"] = page_of_blogs
    context["page_range"] = page_range

    # 上面有了，所以不需要下面这句
    # context["blogs"] = Blog.objects.all()
    context["blogs_num"] = Blog.objects.all().count()
    return render(request, 'blog/all_blog.html', context)


def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog,pk=blog_pk)
    # 方法一
    # blog.readed_num += 1
    # blog.save()

    # 方法二

    if ReadNum.objects.filter(blog=blog).count():
        # 存在记录
        readnum = ReadNum.objects.get(blog=blog)
    else:
        readnum = ReadNum(blog=blog)

    readnum.read_num += 1
    readnum.save()

    # 获取评论
    # blog_content_type = ContentType.objects.get_for_model(blog)
    # comments = Comment.objects.filter(content_type=blog_content_type, object_id=blog.pk, parent=None)

    context["previous_blog"] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context["next_blog"] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context["blog"] = blog
    context["login_form"] = LoginForm()
    # 设置回复倒叙
    # context["comments"] = comments.order_by('-comment_time')

    # context["comments_count"] = Comment.objects.filter(content_type=blog_content_type, object_id=blog.pk).count()
    data = {}
    # 获取对象的model
    # data["content_type"] = blog_content_type.model
    # data["object_id"] = blog_pk
    # 在前端初始化值
    # context["comment_form"] = CommentForm(initial={"content_type": blog_content_type.model, "object_id": blog_pk, "reply_comment_id": 0})
    return render(request, 'blog/blog_detail.html', context)


def blog_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    all_blogs_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(all_blogs_list, 2)
    page_num = request.GET.get("page", 1)
    # get_page方法用于控制不是数字类型，默认返回页面1
    page_of_blogs = paginator.get_page(page_num)

    # 获取当前页
    current_page_num = page_of_blogs.number

    # 获取前后四页的范围
    page_range = list(range(max(current_page_num - 3, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 3, paginator.num_pages) + 1))

    # 加上省略标记
    if page_range[0] - 1 >= 4:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 4:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)

    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context["blogs"] = Blog.objects.filter(blog_type=blog_type)
    context["blogs_num"] = Blog.objects.filter(blog_type=blog_type).count()
    context["blog_type"] = blog_type
    context["page_of_blogs"] = page_of_blogs
    context["page_range"] = page_range
    return render(request, 'blog/blog_with_type.html', context)





