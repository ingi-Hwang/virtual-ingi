# Generated by Django 4.0.3 on 2022-05-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_remove_user_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(null=True),
        ),
    ]