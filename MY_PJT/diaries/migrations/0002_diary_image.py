# Generated by Django 4.2.11 on 2024-03-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
