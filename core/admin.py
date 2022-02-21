from django.contrib import admin
from .models import Employee, Point


class PointAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'day_of_week',
        'date',
    )


admin.site.register(Employee)
admin.site.register(Point, PointAdmin)

