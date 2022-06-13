# Generated by Django 3.2.13 on 2022-06-13 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_predict', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_id', to='price_predict.product')),
            ],
        ),
    ]
