# Generated by Django 3.1.6 on 2021-02-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='heading_image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media/post/'),
        ),
    ]
