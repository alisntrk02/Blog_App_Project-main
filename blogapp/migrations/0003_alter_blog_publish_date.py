# Generated by Django 5.0.1 on 2024-01-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
