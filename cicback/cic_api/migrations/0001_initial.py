# Generated by Django 5.0.3 on 2024-03-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrayModel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Value', models.IntegerField()),
            ],
        ),
    ]