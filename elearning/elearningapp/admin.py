from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Selection)
admin.site.register(Resource)
admin.site.register(Update)