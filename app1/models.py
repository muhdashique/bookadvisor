from django.db import models

class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Add this if the description field is needed
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


