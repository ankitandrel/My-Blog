# Generated by Django 3.1.6 on 2021-02-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210217_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_category',
            field=models.CharField(choices=[('Web_Design', 'Web_Design'), ('HTML', 'HTML'), ('Freebies', 'Freebies'), ('JavaScript', 'JavaScript'), ('CSS', 'CSS'), ('Tutorials', 'Tutorials')], default='....', max_length=155),
        ),
    ]