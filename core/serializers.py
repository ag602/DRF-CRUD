from rest_framework import serializers
from .models import User, Task
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(email=self.validated_data['username'],username=self.validated_data['username'],
                          name=self.validated_data['name']
                          )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password Mismatched'})
        user.set_password(password)
        user.save()
        return user


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#
#         # Add custom claims
#         token['email'] = user.email
#         print(token)
#         return token


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': False}
        }

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            username = authenticate(request=self.context.get('request'),
                                email=username, password=password)
            if not username:
                msg = _("Credentials don't match!")
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['username'] = username
        print(data['username'])
        return data
    #
    # def create(self, validated_data):
    #     return CustomUser.objects.create(**validated_data)


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
