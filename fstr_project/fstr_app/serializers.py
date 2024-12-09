from rest_framework import serializers
from .models import Pass

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = '__all__'
        read_only_fields = ('status',)
