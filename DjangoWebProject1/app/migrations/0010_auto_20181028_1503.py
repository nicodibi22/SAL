# Generated by Django 2.1.2 on 2018-10-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181028_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodo_no_led',
            name='lampara',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Lampara_No_LED'),
        ),
    ]