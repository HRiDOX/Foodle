# Generated by Django 4.1 on 2022-12-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_tax_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]