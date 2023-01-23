from rest_framework import serializers
from .models import Entry


class Login_serializers(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
