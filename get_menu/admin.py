from django.contrib import admin
from .models import cookbook
# Register your models here.


class TestAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(cookbook, TestAdmin)