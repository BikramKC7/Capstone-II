# Generated by Django 5.1.1 on 2024-11-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_highest_sentiment_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='highest_sentiment_percentage',
            field=models.CharField(max_length=100),
        ),
    ]