# Generated by Django 3.0.5 on 2021-03-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_code',
            field=models.PositiveIntegerField(null=True),
        ),
    ]