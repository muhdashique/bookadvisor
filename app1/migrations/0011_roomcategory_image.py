# Generated by Django 4.2.2 on 2024-12-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_room_alter_roomcategory_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_categories/'),
        ),
    ]