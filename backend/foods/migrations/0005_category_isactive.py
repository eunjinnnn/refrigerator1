# Generated by Django 5.0.3 on 2024-06-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_remove_category_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]