# Generated by Django 2.1.1 on 2018-09-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180906_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Location',
        ),
        migrations.AddField(
            model_name='post',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
