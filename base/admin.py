from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Currency)
admin.site.register(Message)