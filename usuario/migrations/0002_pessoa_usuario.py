# Generated by Django 3.0.2 on 2020-02-03 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='usuario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
