# Generated by Django 3.1.1 on 2020-09-04 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_processimage_palette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processimage',
            name='palette',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
