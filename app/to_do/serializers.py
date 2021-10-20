from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import Group, User
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class TaskListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Task
        fields = ('id', 'title', 'deadline')


class TaskDetailSerializer(serializers.ModelSerializer) :
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta :
        model = Task
        fields = '__all__'

#check V2

class MyTokenObtainPairSerializer(TokenObtainPairSerializer) :

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True)
    group = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'group')


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],

        )


        group = validated_data['group']
        my_group = Group.objects.get(name=group)
        my_group.user_set.add(user)

        user.set_password(validated_data['password'])
        user.save()

        return user

