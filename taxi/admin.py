from django.contrib import admin
from taxi.models import Car, Expences, TO_History, Margin, Report

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Expences)
class ExpencesAdmin(admin.ModelAdmin):
    pass


@admin.register(TO_History)
class TO_HistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Margin)
class MarginAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass
