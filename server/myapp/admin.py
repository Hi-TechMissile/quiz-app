from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    model = User
    filter_horizontal = ('remaining_questions',)  # Add this line to make it easier to select multiple questions

admin.site.register(User, UserAdmin)
admin.site.register(Question)