from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse

class CustomManager(BaseUserManager):
    def create_user(self, username, email, password, age, address, **extra_fields):
        if not email:
            raise ValueError(_("This is mandatory field"))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, age=age, address=address, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, age, address, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Super user must have is_superuser=True"))
        if not extra_fields.get("is_staff"):
            raise ValueError(_("Super user must have is_staff=True"))
        return self.create_user(username, email, password, age, address, **extra_fields)

class CustomUser(AbstractUser):
    fullname = models.CharField(_("Full Name"), max_length=200, blank=True, default="")
    email = models.EmailField(default="")
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=300, default="")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['fullname', 'email', 'age', 'address']
    objects = CustomManager()

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={'pk':self.id})
