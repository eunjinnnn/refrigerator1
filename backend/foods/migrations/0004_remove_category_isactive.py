# Generated by Django 5.0.3 on 2024-06-11 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_category_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='isactive',
        ),
    ]
