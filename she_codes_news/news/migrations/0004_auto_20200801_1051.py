# Generated by Django 3.0.8 on 2020-08-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200801_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
