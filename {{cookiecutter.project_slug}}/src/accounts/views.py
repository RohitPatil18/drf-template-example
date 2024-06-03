from rest_framework import generics

from accounts import serializers
from core.mixins import PublicAPIMixin


class UserRegistrationAPIView(PublicAPIMixin, generics.CreateAPIView):
    """
    User registration API. This endpoint should be used to allow
    new registration.
    """

    serializer_class = serializers.UserCreateSerializer