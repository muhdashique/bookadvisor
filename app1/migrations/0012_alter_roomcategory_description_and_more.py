# Generated by Django 4.2.2 on 2024-12-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_roomcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='roomcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='roomcategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]