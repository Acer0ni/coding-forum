from django.contrib import admin
from .models import User
from .models.thread import Thread
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Thread)