# Generated by Django 4.1.2 on 2022-10-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_user_nuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='', upload_to='images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('caption', models.CharField(default='', max_length=200)),
                ('userid', models.CharField(max_length=30)),
            ],
        ),
    ]
