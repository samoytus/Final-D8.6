# Generated by Django 4.1.6 on 2023-09-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='Default author', max_length=255, verbose_name='имя автора'),
        ),
    ]
