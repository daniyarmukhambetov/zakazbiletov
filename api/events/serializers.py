from rest_framework import serializers
from .models import Event, Seat, Category, Comment


class EventListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ["id", "name", "begins_date", "begins_time", "city", "address", "category", "has_bonuses"]


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["name", "count", "price"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ["id", "content", "author"]


class EventSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, source='event_seats')
    comments = CommentSerializer(many=True, source='event_comments')
    # seats_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ["id", "name", "begins_date", "begins_time", "city", "address", "category", "seats", "comments",
                  "has_bonuses", ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]
