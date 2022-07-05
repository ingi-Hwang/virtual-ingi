# Generated by Django 4.0.3 on 2022-05-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('W', '여성')], default='', max_length=2, verbose_name='성별'),
        ),
    ]
