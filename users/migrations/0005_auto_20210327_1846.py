# Generated by Django 3.0.5 on 2021-03-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210326_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]