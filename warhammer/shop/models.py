from django.db import models
from django.shortcuts import reverse


class Categories(models.Model):
    name = models.CharField(
            verbose_name='Название',
            max_length=50
        )
    slug = models.SlugField(
            max_length=50,
            db_index=True
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


    class Meta:
        default_related_name = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['slug']


class Tags(models.Model):
    name_tag = models.CharField(
            verbose_name='Тег',
            max_length=50,
            db_index=True
        )
    slug = models.SlugField(max_length=50, db_index=True)

    def __str__(self):
        return self.name_tag

    class Meta:
        default_related_name = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['slug']


class Orders(models.Model):
    title = models.CharField(
            verbose_name='Заголовок',
            max_length=200
        )
    slug = models.SlugField(
            db_index=True,
            max_length=200
        )
    price = models.SmallIntegerField(
            verbose_name='Цена'
        )
    description = models.TextField(
            verbose_name='Описание'
        )
    image = models.ImageField(
            upload_to='photos/%Y/%m/%d',
            verbose_name='Фото'
        )
    time_create = models.DateField(
            auto_now_add=True,
            verbose_name='Дата'
        )
    is_published = models.BooleanField()
    category = models.ForeignKey(
            'Categories',
            verbose_name='Категория',
            on_delete=models.CASCADE,
            related_name='category',
        )
    tags = models.ManyToManyField(
            'Tags',
            verbose_name='Теги',
            related_name='tags'
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'
        ordering = ['title']


class Comments(models.Model):
    order = models.ForeignKey(
            'Orders',
            verbose_name='Обьявление',
            related_name='comment',
            on_delete=models.CASCADE,
            null=True,
        )
    user_name = models.CharField(
            verbose_name='Имя',
            max_length=100,
            null=True
        )
    email = models.EmailField(
            verbose_name='Почта',
            max_length=100,
            null=True
        )
    content = models.CharField(
            verbose_name='Содержание',
            max_length=500,
            null=True
        )

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
