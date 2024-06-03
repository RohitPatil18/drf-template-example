from rest_framework import serializers

from accounts.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email_address", "user_type")

class ConfirmPasswordInMixin(serializers.Serializer):
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if validated_data.get("password") != validated_data.get("confirm_password"):
            raise serializers.ValidationError(
                {"password": "Password and Confirm Password do not match."}
            )
        validated_data.pop("confirm_password")
        return validated_data


class UserCreateSerializer(ConfirmPasswordInMixin, serializers.ModelSerializer):
    """
    Serializer for `User Registration` API
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email_address",
            "password",
            "confirm_password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }