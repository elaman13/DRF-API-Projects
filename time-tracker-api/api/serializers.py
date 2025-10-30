from datetime import timezone
from rest_framework import serializers
from app.models import Time

class TimeSerializer(serializers.Serializer):
    start_time = serializers.BooleanField(required=False)
    end_time = serializers.BooleanField(required=False)

    def create(self, validated_data):
        start_time = timezone.now() if validated_data.get('start_time') else None
        
        end_time = timezone.now() if validated_data.get('end_time') else None

        return Time.objects.create(start_time=start_time, end_time=end_time)
    
    def update(self, instance, validated_data):
        end_time = timezone.now() if validated_data.get('endtime') else None
        instance.end_time = end_time
        instance.save()

        return Time.objects.update()

class TimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'