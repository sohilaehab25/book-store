# Generated by Django 5.0.4 on 2024-04-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_rename_tags_book_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]