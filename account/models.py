import uuid

from django.conf import settings
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'countries'
        verbose_name = 'country'
        ordering = ['name']
        db_table = 'countries'


class State(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'states'
        verbose_name = 'state'
        ordering = ['name']
        db_table = 'states'
        unique_together = (('name', 'abbreviation'),)


class City(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'cities'
        verbose_name = 'city'
        ordering = ['name']
        db_table = 'cities'
        unique_together = (('name', 'abbreviation'),)


class Location(models.Model):
    pass


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    country = models.ForeignKey(to=Country, blank=True, null=True, on_delete=models.CASCADE, related_name='+')
    state = models.ForeignKey(to=State, blank=True, null=True, on_delete=models.CASCADE, related_name='+')
    city = models.ForeignKey(to=City, blank=True, null=True, on_delete=models.CASCADE, related_name='+')
    avatar = models.ImageField(blank=True, null=True)


class Email(models.Model):
    pass


class Divice(models.Model):
    DIVICE_WEB = 1
    DIVICE_TV = 2
    DIVICE_IOS = 3
    DIVICE_ANDROID = 4
    DIVICE_PC = 5
    DIVICE_CHOICES = (
        (DIVICE_WEB, 'Web'),
        (DIVICE_TV, 'TV'),
        (DIVICE_IOS, 'IOS'),
        (DIVICE_ANDROID, 'Android'),
        (DIVICE_PC, 'PC')
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE)
    device_type = models.PositiveSmallIntegerField(choices=DIVICE_CHOICES, default=DIVICE_WEB)
    device_uuid = models.UUIDField('device UUID', unique=True, default=uuid.uuid4, editable=False)
    last_login = models.DateTimeField('last login date', null=True)
    date_joined = models.DateTimeField('date joined', null=True)
    device_os = models.CharField('device OS', max_length=20, choices=DIVICE_CHOICES, default=DIVICE_WEB)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    device_model = models.CharField('device model', max_length=20, blank=True)
    app_version = models.CharField('app version', max_length=20, blank=True)
