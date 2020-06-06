from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user """

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #hash the password, encrypted
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details in the constructor"""
        user = self.create_user(email,name,password)

        #is_superuser is automatically by PermissionsMixin
        #while we defined the is_staff
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    #we want an email column with specific max length and be unique
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #to see if user profile is activated or not, by default it is activated
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #instead of username and password, it will be email and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name #as name is merged in one thing

    #when converting this class to string
    def __str__(self):
        """Return string representation of our user"""
        return self.email
        #note: this is recommended for all django models
