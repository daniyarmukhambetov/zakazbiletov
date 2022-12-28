# Generated by Django 4.1.4 on 2022-12-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('CANCELLED', 'CANCELLED'), ('FAILED', 'FAILED')], default='SUCCESS', max_length=64),
        ),
    ]