from django.contrib.auth.models import AbstractUser
from django.db import models
from .services import Avatar


class User(AbstractUser):
    avatar = models.ImageField(
        verbose_name="avatar",
        default="/static/main/image/avatar-default-icon.png",
        upload_to=Avatar.path_to_save,
    )
