from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Store(models.Model):

    name = models.CharField(max_length=100)
    uploaded_file = models.FileField(
        upload_to="uploads/",
    )
    converted_file = models.FileField(
        upload_to="converted_files", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
