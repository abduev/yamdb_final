from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import UserProfile

from .validators import year_validator


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            verbose_name='Название категории')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            verbose_name='Название жанра')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Название произведения')
    year = models.PositiveSmallIntegerField(blank=True, null=True,
                                            validators=[year_validator],
                                            verbose_name='Год выхода')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='titles', blank=True, null=True,
                                 verbose_name='Категория')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')

    class Meta:
        ordering = ['-year']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField(blank=False, null=False,
                            verbose_name='Текст ревью')
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reviews',
        verbose_name='Автор'
    )
    score = models.IntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10)),
        blank=False, null=False, verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Ревью'
        verbose_name_plural = 'Ревью'


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Ревью'
    )
    text = models.TextField(blank=False, null=False,
                            verbose_name='Текст комментария')
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
