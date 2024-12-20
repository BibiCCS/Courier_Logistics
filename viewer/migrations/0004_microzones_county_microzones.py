# Generated by Django 4.2 on 2024-12-15 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_alter_courier_neighborhood_alter_neighborhood_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microzones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='county',
            name='microzones',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='microzones', to='viewer.microzones'),
        ),
    ]
