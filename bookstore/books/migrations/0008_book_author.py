# Generated by Django 5.0.4 on 2024-04-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
