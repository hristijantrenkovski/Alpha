# Generated by Django 4.0.4 on 2022-07-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_profile_address_profile_facebook_profile_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lives_at',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
