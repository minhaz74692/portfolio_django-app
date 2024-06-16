from django.contrib import admin
from about_us.models import User

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('userId', 'userName','email', 'age', 'profession')

admin.site.register(User, TeacherAdmin)