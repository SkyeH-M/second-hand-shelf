# Generated by Django 3.2.19 on 2023-06-22 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_rename_average_rating_product_averagerating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price_factor', models.DecimalField(decimal_places=2, max_digits=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Qualities',
            },
        ),
    ]
