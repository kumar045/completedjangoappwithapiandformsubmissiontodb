# Generated by Django 3.0.8 on 2020-07-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
