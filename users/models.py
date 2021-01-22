from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    COACH = 'CH'
    PLAYER = 'PR'
    USER_TYPE_CHOICES = [
        (COACH, 'Coach'),
        (PLAYER, 'Player'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=PLAYER,
    )

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
