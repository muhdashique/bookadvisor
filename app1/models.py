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

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} - {self.subject}"

