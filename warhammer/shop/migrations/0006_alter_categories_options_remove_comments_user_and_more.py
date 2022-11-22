# Generated by Django 4.1.3 on 2022-11-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_categories_options_alter_tags_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'default_related_name': 'category', 'ordering': ['slug'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_name',
            field=models.CharField(help_text='Введите имя', max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(help_text='Введите комментарий', max_length=500, null=True, verbose_name='Содержание'),
        ),
    ]