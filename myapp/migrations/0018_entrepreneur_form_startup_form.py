# Generated by Django 4.1.2 on 2022-11-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_image_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneur',
            name='form',
            field=models.URLField(blank=True, default='www.google.com', null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='form',
            field=models.URLField(blank=True, null=True),
        ),
    ]
