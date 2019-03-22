# Generated by Django 2.1.7 on 2019-02-24 20:47

from django.db import migrations, models
import location_field.models.plain
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
    ]
