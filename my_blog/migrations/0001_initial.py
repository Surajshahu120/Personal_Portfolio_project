# Generated by Django 4.1.3 on 2023-01-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('Date', models.DateField()),
            ],
        ),
    ]
