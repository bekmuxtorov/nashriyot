# Generated by Django 4.0.6 on 2022-09-19 04:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_articles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Maqola matni:'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('1', 'Mahalliy'), ('2', 'Dunyo'), ('3', 'Moliya'), ('4', 'Sport'), ('5', 'Fan-Texnika')], default=1, max_length=35),
        ),
    ]
