# Generated by Django 4.2.5 on 2023-10-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imgpath',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]