# Generated by Django 4.2.2 on 2024-12-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_room_name_alter_room_category_alter_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
    ]
