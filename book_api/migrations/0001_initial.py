# Generated by Django 5.0.7 on 2024-08-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('page_number', models.IntegerField()),
                ('publish_date', models.DateField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
