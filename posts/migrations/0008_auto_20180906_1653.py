# Generated by Django 2.1.1 on 2018-09-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_print1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='print2',
            field=models.CharField(default='some string', max_length=120),
        ),
        migrations.AddField(
            model_name='post',
            name='print3',
            field=models.CharField(default='some string', max_length=120),
        ),
        migrations.AddField(
            model_name='post',
            name='print4',
            field=models.CharField(default='some string', max_length=120),
        ),
        migrations.AddField(
            model_name='post',
            name='print5',
            field=models.CharField(default='some string', max_length=120),
        ),
    ]
