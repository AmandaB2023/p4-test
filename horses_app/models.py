from django.db import models
from cloudinary.models import CloudinaryField


class Horse(models.Model):
    name = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    breed = models.TextField()
    colour = models.TextField()
    about = models.TextField()
    year_of_birth = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name} | {self.breed}"