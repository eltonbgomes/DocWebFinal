# Generated by Django 3.0.2 on 2020-02-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('idade', models.CharField(blank=True, max_length=3, null=True)),
                ('cep', models.CharField(max_length=8)),
                ('endereco', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=2)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('biografia', models.TextField(blank=True, null=True)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
    ]
