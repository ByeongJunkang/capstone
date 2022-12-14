# Generated by Django 4.1.2 on 2022-11-12 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstone.question')),
            ],
        ),
    ]
