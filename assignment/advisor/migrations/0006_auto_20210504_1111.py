# Generated by Django 3.2 on 2021-05-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0005_alter_advisor_photo_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calls',
            old_name='advisor',
            new_name='advisorid',
        ),
        migrations.RenameField(
            model_name='calls',
            old_name='user',
            new_name='userid',
        ),
    ]
