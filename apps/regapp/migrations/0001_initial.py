# Generated by Django 3.2.5 on 2021-10-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('regcode', models.CharField(default='', max_length=128, unique=True)),
                ('opcode', models.CharField(choices=[('update', 'update'), ('create', 'create')], default='create', max_length=32)),
                ('sub', models.CharField(default='', max_length=128, unique=True)),
                ('linked_sub', models.CharField(default='', max_length=128, unique=True)),
                ('linked_iss', models.CharField(default='', max_length=128)),
                ('linked_idp_name', models.CharField(default='', max_length=128)),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('username', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
