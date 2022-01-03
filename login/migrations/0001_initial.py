# Generated by Django 4.0 on 2022-01-03 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=10)),
                ('UserPassword', models.CharField(max_length=8)),
                ('UserPicture', models.CharField(max_length=255)),
                ('UserType', models.BooleanField()),
                ('UserEmail', models.EmailField(max_length=254)),
            ],
        ),
    ]