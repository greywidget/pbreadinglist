# Generated by Django 2.0.7 on 2018-07-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20180729_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booknote',
            name='private',
        ),
        migrations.AddField(
            model_name='booknote',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]