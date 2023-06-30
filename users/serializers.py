from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="This field must be unique.")],
    )
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields =['id', 'password', 'full_name', 'artistic_name','email', 
                 'username']
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
