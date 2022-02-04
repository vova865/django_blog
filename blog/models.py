from django.db import models
from django.urls import reverse


class Article(models.Model):
    """Статья."""
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Контент")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    writer = models.ForeignKey('Writer', on_delete=models.PROTECT, verbose_name="Писатель", null=True)
    # Также нужно добавить кол-во просмотров, поле - views
    #     Article.objects.filter(slug='...').update(views=F('views')+1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'
        ordering = ['id']


class Writer(models.Model):
    """Писатель."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, null=True)
    city = models.CharField(max_length=30, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('writer', kwargs={'writer_id': self.id})

    class Meta:
        verbose_name = 'писателя'
        verbose_name_plural = 'Писатели'
        ordering = ['id']


class Category(models.Model):
    """Категория."""
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']
