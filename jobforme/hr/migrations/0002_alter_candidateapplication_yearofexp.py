# Generated by Django 5.0.4 on 2024-08-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateapplication',
            name='YearOfExp',
            field=models.IntegerField(default=0),
        ),
    ]