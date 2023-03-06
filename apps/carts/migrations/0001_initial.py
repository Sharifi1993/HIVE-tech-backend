# Generated by Django 4.1.3 on 2023-03-06 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('demo', models.CharField(max_length=200, verbose_name='T shirt')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_user', to='users.user')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]