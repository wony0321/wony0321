# Generated by Django 4.2.11 on 2024-03-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0003_rename_image_diary_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='picture',
            field=models.ImageField(blank=True, upload_to='diary/%y/%b/%a'),
        ),
    ]