# Generated by Django 4.1.2 on 2022-10-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kscholar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('attachment_url', models.TextField(blank=True, null=True)),
                ('attachment_content', models.TextField(blank=True, null=True)),
                ('current_url', models.TextField(blank=True, null=True)),
                ('department', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
