# Generated by Django 3.2.9 on 2021-11-16 04:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20211116_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='post_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]