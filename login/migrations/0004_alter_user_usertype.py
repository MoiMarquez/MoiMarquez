# Generated by Django 4.0 on 2022-01-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserType',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
