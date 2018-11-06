from rest_framework import serializers
from todos import models

# Класс отображает поля списка которые будут отображаться
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'email',
            'company',
        )
        model = models.User

