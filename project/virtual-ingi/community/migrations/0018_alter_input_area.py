# Generated by Django 4.0.3 on 2022-06-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0017_alter_input_endperiod_alter_input_startperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='area',
            field=models.CharField(choices=[('B', '부산')], default='', max_length=20, verbose_name='지역'),
        ),
    ]