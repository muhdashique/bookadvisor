# Generated by Django 4.2.2 on 2024-12-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0003_delete_roomcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
