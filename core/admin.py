from django.contrib import admin
from .models import Employee, Point, DayOfWeek


class PointAdmin(admin.ModelAdmin):
    list_display = [
        'employee',
        'day_of_week',
        'date',
        'entrance',
        'left',
    ]


admin.site.register(Employee)
admin.site.register(Point, PointAdmin)
admin.site.register(DayOfWeek)

