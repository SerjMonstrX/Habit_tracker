from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated


from users.models import User
from users.serializers import UserProfileSerializer


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserProfileSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
