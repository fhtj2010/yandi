# Generated by Django 2.0 on 2019-12-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_time'], 'verbose_name': '评论信息', 'verbose_name_plural': '评论信息'},
        ),
    ]