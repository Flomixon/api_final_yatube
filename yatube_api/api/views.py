from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Comment, Follow, User
from .serializers import PostSerializer, GroupSerializer
from .serializers import CommentSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').\
        select_related('group').all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )

    def list(self, request, post_id):
        post = Post.objects.get(id=post_id)
        queryset = post.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        permissions.IsAuthenticated
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
