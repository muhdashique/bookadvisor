from django.db import models

class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # Add description field

    def __str__(self):
        return self.name


class Room(models.Model):
     # Make name field nullable
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rooms/')
    
    def __str__(self):
        return self.name



class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/images/')
    review = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)

    def __str__(self):
        return self.name

