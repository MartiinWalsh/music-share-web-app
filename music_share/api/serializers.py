from rest_framework import serializers
from .models import Room

# Serialize Room object to return as a response
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "id",
            "code",
            "host",
            "guest_can_pause",
            "votes_to_skip",
            "created_at",
        )


# Serialize data from a request
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("guest_can_pause", "votes_to_skip")
