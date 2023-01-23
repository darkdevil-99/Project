from rest_framework import serializers
from .models import Table


class Table_serializers(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['username', 'email', 'password']





