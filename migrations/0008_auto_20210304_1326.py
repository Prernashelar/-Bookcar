# Generated by Django 3.1.4 on 2021-03-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_auto_20210303_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='destination',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='destination',
            name='image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]