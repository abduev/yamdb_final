# Generated by Django 3.0.5 on 2021-03-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210324_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_code',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
    ]