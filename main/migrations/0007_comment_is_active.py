# Generated by Django 3.1.2 on 2020-10-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Выводить на экран?'),
        ),
    ]
