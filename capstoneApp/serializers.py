from rest_framework import serializers
from .models import userinfo


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = ['username', 'userid', 'password']