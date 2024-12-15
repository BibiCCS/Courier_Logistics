# Generated by Django 4.2 on 2024-12-14 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_county_city_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='couriers', to='viewer.neighborhood'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhoods', to='viewer.city'),
        ),
        migrations.AlterField(
            model_name='street',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='viewer.neighborhood'),
        ),
    ]