from django.contrib import admin
from .models import User,Thread,Post

from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Thread)
admin.site.register(Post)