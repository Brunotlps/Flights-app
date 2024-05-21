# Generated by Django 5.0.6 on 2024-05-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_airport_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]
