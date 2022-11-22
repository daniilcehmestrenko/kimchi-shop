# Generated by Django 4.1.3 on 2022-11-21 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_comments_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='shop.categories', verbose_name='Категория'),
        ),
    ]
