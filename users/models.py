from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES_CHOICES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin')
    ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.CharField(max_length=50, unique=True, verbose_name='Почта')
    user_code = models.SlugField(null=True, verbose_name='Код подтверждения')
    bio = models.CharField(
        max_length=500, blank=True, verbose_name='Информация о пользователе'
    )
    role = models.CharField(
        max_length=10, choices=ROLES_CHOICES, default=USER, verbose_name='Роль'
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
