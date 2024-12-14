from django.db import models

class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
