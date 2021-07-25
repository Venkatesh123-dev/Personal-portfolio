# Generated by Django 3.2.5 on 2021-07-21 13:51

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('updated__month',))),
                ('image', models.ImageField(upload_to='portfolio-images')),
                ('port_type', models.CharField(choices=[('web', 'Web'), ('app', 'App')], default='web', max_length=100)),
                ('description', models.TextField()),
                ('live_url', models.URLField(blank=True, null=True)),
                ('source_url', models.URLField(blank=True, null=True)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('updated', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio-screenshots')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio')),
            ],
        ),
    ]
