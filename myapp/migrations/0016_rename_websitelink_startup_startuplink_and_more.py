# Generated by Django 4.1.2 on 2022-11-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_entrepreneur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='websitelink',
            new_name='startuplink',
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='phoneno',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='phoneno',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
