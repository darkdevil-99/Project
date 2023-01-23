from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User1
from django.contrib.auth.hashers import make_password


'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ['User', 'First_name', 'Last_name']
'''


class RegisterSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User1.objects.all())]
    )
    Password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    Confirm_Password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User1
        fields = ['Username', 'Password', 'Confirm_Password',
                  'Email', 'First_name', 'Last_name']

        extra_kwargs = {
            'First_name': {'required': True},
            'Last_name': {'required': True}
        }

        def validate(self, attrs):
            if attrs['Password'] != attrs['Confirm_Password']:
                raise serializers.ValidationError(
                    {"Password": "Password fields didn't match."})
            return attrs

        def create(self, validated_data):
            user = User1.objects.create(
                username=validated_data['Username'],
                email=validated_data['Email'],
                first_name=validated_data['First_name'],
                last_name=validated_data['Last_name'],
                password=validated_data['Password']
            )
            user.Password = make_password(user.Password)
            user.save()
            return user








