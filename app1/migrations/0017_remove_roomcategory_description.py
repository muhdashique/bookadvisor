# Generated by Django 4.2.17 on 2024-12-20 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_room_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomcategory',
            name='description',
        ),
    ]
