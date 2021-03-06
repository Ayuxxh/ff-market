# Generated by Django 3.2.9 on 2021-11-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default="static/account/images/profile_picture/default.jpeg'", upload_to='static/account/images/profile_picture/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('customer', 'customer'), ('seller', 'seller')], default='customer', max_length=20),
        ),
    ]
