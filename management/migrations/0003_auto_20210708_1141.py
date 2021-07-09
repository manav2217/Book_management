# Generated by Django 3.2.5 on 2021-07-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20210708_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='book_lan',
        ),
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.RemoveField(
            model_name='book',
            name='b_language',
        ),
        migrations.AddField(
            model_name='book',
            name='b_language',
            field=models.ManyToManyField(to='management.Language'),
        ),
    ]