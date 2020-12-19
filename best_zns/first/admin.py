from django.contrib import admin
from .models import User,Profile,Contact,Call,SMS,Note,File
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Call)
admin.site.register(SMS)
admin.site.register(Note)
admin.site.register(File)
