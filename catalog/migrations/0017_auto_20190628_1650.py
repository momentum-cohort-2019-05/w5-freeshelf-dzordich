# Generated by Django 2.2.2 on 2019-06-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20190627_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
