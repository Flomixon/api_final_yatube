from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/groups', GroupViewSet)
router_v1.register(r'v1/posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet)
router_v1.register('v1/follow', FollowViewSet)

urlpatterns = [
    path('v1/jwt/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls))
]
