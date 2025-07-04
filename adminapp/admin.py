from django.contrib import admin
from .models import News, Program, Branch, Year, Material
# Register your models here.
admin.site.register(News)
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Material)