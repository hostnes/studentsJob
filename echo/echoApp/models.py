from echoApp.validators import message_url_validator
from django.db import models


GENDERS = (
    ("M", "Man"),
    ("W", "Women")
)


CURRENCY = (
    ("USD", "USD"),
    ("USD", "USD"),
    ("RUB", "RUB"),
)


"""#################################### general constants ####################################"""


class Country(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Messenger(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, validators=[message_url_validator])
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


"""###c################################# echo ####################################"""


class User(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.CharField(unique=True, max_length=255)
    username = models.CharField(max_length=230, blank=True, unique=True, null=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True, unique=True, null=True)
    gender = models.CharField(max_length=255, choices=GENDERS,  null=True, default=None)

    img = models.ImageField(upload_to="user_photo", blank=True, default='../static/img/none-logo.png')
    birthday = models.CharField(max_length=10, blank=True, null=True)
    region = models.OneToOneField(Region, on_delete=models.SET_NULL, null=True, blank=True)
    place_of_education = models.ForeignKey(Education, on_delete=models.CASCADE, null=True, blank=True)

    publish_phone = models.BooleanField(default=False)
    public_status = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Company(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="company", blank=True)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    celery = models.PositiveIntegerField()
    currency = models.CharField(max_length=255, choices=CURRENCY,  null=True, default=None)
    date_of_create = models.DateField(auto_now_add=True)

    city = models.ForeignKey(Region, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    photo = models.ImageField(upload_to='user_photos/', default='user_photos/none-logo.png')
    user = models.CharField(default="User deleted", max_length=20)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.user





"""#################################### echo.job ####################################"""


# class Experience(models.Model):
#     title = models.CharField(max_length=50)

