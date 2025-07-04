from django.contrib import admin

# Register your models here.
from .models import Feedback, Response, Question
admin.site.register(Feedback)
admin.site.register(Response)
admin.site.register(Question)