from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet, CommentViewSet, CategoryViewSet, GenreViewSet, TitleViewSet
)
from users.views import (
    UserViewSet,
    email_confirmation,
    get_token,
)


app_name = 'api'


v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews',
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/auth/email/', email_confirmation, name='email'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/', include(v1_router.urls)),
]
