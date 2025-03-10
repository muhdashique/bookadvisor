# Generated by Django 4.2.2 on 2024-12-21 11:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_roomcategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.roomcategory'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='rooms/'),
            preserve_default=False,
        ),
    ]
