# Generated by Django 4.1 on 2022-12-29 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_alter_seat_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('vendor', 'total_seats', 'avaiable_seats')},
        ),
    ]