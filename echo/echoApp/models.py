from echoApp.validators import message_url_validator
from django.db import models


GENDERS = (
    ("M", "Man"),
    ("W", "Women")
)

"""pbkdf2_sha256$600000$gM89zK5WTmhsDnQy6PEGAh$ntvc6FOnsf/S1X/CctTuKKrcCsCKqRwiWBzyOIN4z8A='"""



"""#################################### general constants ####################################"""


class Country(models.Model):
    title = models.CharField(max_length=255)


class Region(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Messenger(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, validators=[message_url_validator])
    is_publish = models.BooleanField(default=False)


"""#################################### echo ####################################"""


class User(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.CharField(unique=True, max_length=255)
    username = models.CharField(max_length=230, blank=True, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True, unique=True)
    gender = models.CharField(max_length=255, choices=GENDERS,  null=True, default=None)

    img = models.ImageField(upload_to="user", blank=True)
    birthday = models.DateField(blank=True, null=True)
    region = models.OneToOneField(Region, on_delete=models.SET_NULL, null=True, blank=True)

    publish_phone = models.BooleanField(default=False)
    public_status = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Comment(models.Model):
    photo = models.ImageField(upload_to='user_photos/', default='user_photos/none-logo.png')
    user = models.CharField(default="User deleted", max_length=20)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.user

"""#################################### echo.job ####################################"""


# class Experience(models.Model):
#     title = models.CharField(max_length=50)

