# Generated by Django 4.2.5 on 2023-10-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_review_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='\\staticfiles\\images\\placeholder.png', null=True, upload_to=''),
        ),
    ]
