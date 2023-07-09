from django.contrib import admin
from api.models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fields = ['user','first_name','last_name','about','phone','country']
    readonly_fields = ('user',)
    list_display = ('user','__str__')

admin.site.register(Profile,ProfileAdmin)