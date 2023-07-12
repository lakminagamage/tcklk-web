from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, max_length=100, default="")
    image = models.ImageField(default='default.jpg', upload_to='accounts/profile_pics')
    contact_number = models.CharField(blank=False, default='', max_length=13)
    country = models.CharField(blank=False, default='Sri Lanka', max_length=10)
    city = models.CharField(blank=False, max_length=255)
    address = models.CharField(blank=False, max_length=500)
    postal_code = models.CharField(blank=True, max_length=7)
    social_contacts = models.TextField(blank=True)
    about = models.TextField(blank=False, default='')



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self , *args ,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
