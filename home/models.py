from django.db import models
import os

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='static/images/project')
    caption = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True, null=True)   # Add this field to store the link for each image
    # Add more fields as needed

    def __str__(self):
        return self.caption
    
    def delete(self, *args, **kwargs):
        # Delete the image file when the object is deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)



