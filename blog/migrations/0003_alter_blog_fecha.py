# Generated by Django 4.0 on 2024-08-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
