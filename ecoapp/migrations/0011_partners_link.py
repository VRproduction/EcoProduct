# Generated by Django 4.2.7 on 2023-11-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0010_rename_category_blog_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='link',
            field=models.CharField(blank=True, max_length=2050, null=True),
        ),
    ]
