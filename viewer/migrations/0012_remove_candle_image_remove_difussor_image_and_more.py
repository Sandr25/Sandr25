# Generated by Django 4.2.13 on 2024-08-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0011_difussor_image_gift_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candle',
            name='image',
        ),
        migrations.RemoveField(
            model_name='difussor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='essential_oil',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gift_card',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
