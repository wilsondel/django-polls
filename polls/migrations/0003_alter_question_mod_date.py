# Generated by Django 3.2.11 on 2022-04-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220414_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
