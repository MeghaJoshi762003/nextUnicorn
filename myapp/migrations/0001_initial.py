# Generated by Django 4.1.2 on 2022-10-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=122)),
                ('password', models.CharField(max_length=30)),
                ('userid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('post', models.CharField(max_length=20)),
            ],
        ),
    ]
