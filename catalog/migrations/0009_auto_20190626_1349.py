# Generated by Django 2.2.2 on 2019-06-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190626_0320'),
    ]

    operations = [
        migrations.DeleteModel(
            'Book'
        ),
        migrations.DeleteModel(
            "Category"
        ),
    ]