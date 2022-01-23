from django.contrib import admin


from django.contrib import admin
from .models import django_rack,python_rack,math_rack


class djangoadmin(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(django_rack,djangoadmin)


class pythonadmin(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(python_rack,pythonadmin)

class mathadmin(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(math_rack,mathadmin)
