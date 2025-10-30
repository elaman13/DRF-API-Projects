from django.utils import timezone
from rest_framework import serializers
from app.models import Time

class TimeSerializer(serializers.ModelSerializer):
    start = serializers.BooleanField(write_only=True, required=False)
    end = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Time
        fields = ['id', 'start_time', 'end_time', 'start', 'stop']
        read_only_fields = ['start_time', 'end_time']

    def create(self, validated_data):
        if validated_data.get('start'):
            return Time.objects.create(start_time=timezone.now())
        raise serializers.ValidationError("must provide 'start': true to start timer.")
        
    def update(self, instance, validated_data):
        if validated_data.get('stop'):
            instance.end_time = timezone.now()
            instance.save()

        return instance