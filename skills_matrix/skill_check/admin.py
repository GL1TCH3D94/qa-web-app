from django.contrib import admin

from .models import User, Skills, Subject

admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Skills)
