# Generated by Django 4.1.2 on 2022-10-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_log_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='Userid',
            field=models.CharField(default='User', max_length=115, primary_key=True, serialize=False),
        ),
    ]
