from django.db import models

from users.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(null=False, max_length=255)
    begins_time = models.TimeField()
    begins_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name="event_category", on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    has_bonuses = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Seat(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    event = models.ForeignKey(Event, related_name="event_seats", on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_comments")
#
# class Ticket(models.Model):
#     price = models.IntegerField()
#     seat_number = models.IntegerField()
