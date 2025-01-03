# Generated by Django 4.2.17 on 2024-12-14 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='room_images/')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='roomcategory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='roomcategory',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='app1.roomcategory'),
        ),
    ]
