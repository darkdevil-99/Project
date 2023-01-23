# Generated by Django 4.1.4 on 2023-01-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.TextField()),
                ('Confirm_Password', models.TextField()),
                ('First_name', models.TextField()),
                ('Last_name', models.TextField()),
            ],
        ),
    ]