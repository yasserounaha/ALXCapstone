# Generated by Django 4.2.1 on 2023-06-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cin',
            field=models.CharField(default='nothing', max_length=20),
            preserve_default=False,
        ),
    ]
