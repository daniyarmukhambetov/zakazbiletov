from rest_framework import serializers

from .models import Payment
from events.models import Seat, Event


class PaymentSerializer(serializers.ModelSerializer):
    cc_number_hidden = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = [
            "id",
            "purchaser_email",
            "purchaser_number",
            "event",
            "seat",
            "cc_number_hidden",
            "created_time",
            "status",
            "count",
        ]
        read_only_fields = [
            "id",
            "id",
            "purchaser_email",
            "purchaser_number",
            "event",
            "seat",
            "cc_number_hidden",
            "created_time",
            "count"
        ]

    def validate_status(self, value):
        if value != 'CANCELLED':
            raise serializers.ValidationError("Invalid status")
        return value

    # @staticmethod
    def get_cc_number_hidden(self, obj):
        return obj.cc_number


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "purchaser_email",
            "purchaser_number",
            "event",
            "seat",
            "count",
            "cc_number",
            "cc_expiry",
            "cc_code",
        ]

    # @staticmethod
    def validate_cc_number(self, value):
        return value

    def create(self, validated_data):
        event = validated_data.get("event")
        seat = validated_data.get("seat")
        if seat.event.pk != event.pk:
            raise serializers.ValidationError("Invalid event or seat")
        if seat.count < validated_data.get("count"):
            raise serializers.ValidationError("Invalid seat count")
        if self.context.get("request").user.is_authenticated and event.has_bonuses:
            self.context.get("request").user.bonuses += seat.price * validated_data.get("count") // 100
            self.context.get("request").user.save()
        seat.count -= validated_data.get("count")
        seat.save()
        return super(PaymentCreateSerializer, self).create(validated_data)
