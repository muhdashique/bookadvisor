# Generated by Django 4.2.2 on 2024-12-28 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_remove_testimonial_destination_background_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='background_image',
        ),
    ]
