from rest_framework import serializers
from .models import Activity, LANGUAGE_CHOICES, STYLE_CHOICES

class ActivitySerializer(serializers.Serializer):
    id = serializers.UUIDField(primary_key=True)
    user_id = serializers.CharField(max_length=20)
    sport_type_id = serializers.CharField(max_length=10)
    creation_application_id = serializers.CharField(max_length=10)
    version = serializers.IntegerField()
    duration = serializers.IntegerField()
    pause = serializers.IntegerField()
    calories = serializers.IntegerField()
    subjective_feeling = serializers.CharField(max_length=20)
    dehydration_volume = serializers.IntegerField()
    plausible = serializers.BooleanField()
    start_time_timezone_offset = serializers.BigIntegerField()
    end_time_timezone_offset = serializers.BigIntegerField()
    tracking_method = serializers.CharField(max_length=20)
    start_time = serializers.BigIntegerField()
    end_time = serializers.BigIntegerField()
    user_perceived_start_time = serializers.BigIntegerField()
    user_perceived_end_time = serializers.BigIntegerField()
    created_at = serializers.BigIntegerField()
    updated_at = serializers.BigIntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Activity.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.sport_type_id = validated_data.get('sport_type_id', instance.sport_type_id)
        instance.creation_application_id = validated_data.get('creation_application_id', instance.creation_application_id)
        instance.creation_application_id = validated_data.get('creation_application_id', instance.creation_application_id)
        instance.version = validated_data.get('creation_application_id', instance.creation_application_id)
        instance.version = validated_data.get('version', instance.version)
        instance.pause = validated_data.get('pause', instance.pause)
        instance.calories = validated_data.get('calories', instance.creation_application_id)
        instance.subjective_feeling = validated_data.get('subjective_feeling', instance.subjective_feeling)
        instance.dehydration_volume = validated_data.get('dehydration_volume', instance.dehydration_volume)
        instance.plausible = validated_data.get('plausible', instance.plausible)
        instance.start_time_timezone_offset = validated_data.get('start_time_timezone_offset', instance.start_time_timezone_offset)
        instance.end_time_timezone_offset = validated_data.get('end_time_timezone_offset', instance.end_time_timezone_offset)
        instance.tracking_method = validated_data.get('tracking_method', instance.tracking_method)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.user_perceived_start_time = validated_data.get('user_perceived_start_time', instance.user_perceived_start_time)
        instance.user_perceived_end_time = validated_data.get('user_perceived_end_time', instance.user_perceived_end_time)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


