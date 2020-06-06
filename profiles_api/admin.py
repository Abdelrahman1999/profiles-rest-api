from django.contrib import admin

from profiles_api import models

#we need to register newly created models with django admin so it knows that you want to display that model in the admin interface
admin.site.register(models.UserProfile)
