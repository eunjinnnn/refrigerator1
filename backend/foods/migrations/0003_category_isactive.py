# Generated by Django 5.0.3 on 2024-06-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_foodunit_alter_fooditem_purchase_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
