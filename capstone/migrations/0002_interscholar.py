# Generated by Django 4.1.2 on 2022-11-20 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interscholar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstone.kscholar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
