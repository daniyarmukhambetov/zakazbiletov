from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    bonuses = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'bonuses']

    def get_bonuses(self, obj):
        return obj.user.bonuses

    def create(self, validated_data):
        user = self.context.get("request").user
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
