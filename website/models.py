from django.db import models
from PIL import Image

class ContactFormModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(blank=False, default="", max_length=500)
    contact_number = models.CharField(blank=False, default="", max_length=13)
    message = models.TextField(blank=False, default="" , max_length=10000)


class PortfolioItems(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=20)
    image = models.ImageField(default='Defportf.jpg', upload_to='portfolio/')
    sort_by = models.CharField(max_length=20, default="")
    keyword = models.CharField(max_length=20, default="")



    def save(self , *args ,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 800:
            output_size = (800, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)


class TestimonialItems(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default='Deftesti.jpg', upload_to='testimonials/')
    business_name = models.CharField(max_length=200)
    message = models.CharField( default="", max_length=500)
    sort_by = models.CharField(max_length=20, default="")
    keyword = models.CharField(max_length=20, default="")
    contact_number = models.CharField(blank=True, max_length=13)
    email = models.EmailField(blank=True)


    def save(self , *args ,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ClientlogoItems(models.Model):
    business_name = models.CharField(max_length=70)
    sort_by = models.CharField(max_length=20, default="")
    keyword = models.CharField(max_length=20, default="")
    image = models.ImageField(default='Defclilog.jpg', upload_to='clientlogo/')

    def save(self , *args ,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 550 or img.width > 750:
            output_size = (750, 550)
            img.thumbnail(output_size)
            img.save(self.image.path)


