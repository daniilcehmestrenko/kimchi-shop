# Generated by Django 4.1.3 on 2022-11-21 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_orders_category_remove_orders_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='shop.orders', verbose_name='Обьявление'),
        ),
    ]
