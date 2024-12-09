from rest_framework import serializers
from .models import Pass

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = '__all__'
        read_only_fields = ('status', 'created_at')

    def update(self, instance, validated_data):
        # Проверка статуса перед обновлением
        if instance.status != 'new':
            raise serializers.ValidationError("Можно редактировать только записи со статусом 'new'")

        # Запрет редактирования определенных полей
        for field in ['user', 'created_at']:
            validated_data.pop(field, None)

        return super().update(instance, validated_data)