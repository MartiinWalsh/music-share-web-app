from django.db import models
import string
import random


def generate_unique_room_code():
    length = 7

    while True:
        # Generate random code of predefined length, only containing uppercase ascii chars
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        # Check if code is unique across rooms
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


# Create your models here.
class Room(models.Model):
    code = models.CharField(
        max_length=8, default=generate_unique_room_code, unique=True
    )
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
