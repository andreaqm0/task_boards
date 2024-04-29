from rest_framework import serializers

from tasks.serializers import TaskSerializer
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    tasks= TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')