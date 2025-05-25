from django.db import models


class BusinessInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    rating = models.FloatField()
    review_count = models.IntegerField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cuisines/')  # Ensure media setup
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class OpeningHour(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    pickup_time = models.CharField(max_length=50)
    delivery_time = models.CharField(max_length=50)

    def __str__(self):
        return self.day
