# Generated by Django 4.1.2 on 2022-10-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_post_log_post_rename_userid_log_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='Userid',
            field=models.CharField(max_length=115, primary_key=True, serialize=False),
        ),
    ]