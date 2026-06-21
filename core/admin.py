from django.contrib import admin
from .models import City, District, EducationLevel, SchoolType, AcademicYear, School
from jalali_date.admin import ModelAdminJalaliMixin
class RTLAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin/css/rtl.css",)
        }

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "is_active")
    list_filter = ("city", "is_active")
    search_fields = ("name", "city__name")


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(SchoolType)
class SchoolTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(AcademicYear)
class AcademicYearAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("-start_date",)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "district",
        "education_level",
        "school_type",
        "phone_number",
        "is_active",
    )

    list_filter = (
        "district__city",
        "district",
        "education_level",
        "school_type",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "district__name",
        "district__city__name",
    )

    autocomplete_fields = (
        "district",
        "education_level",
        "school_type",
    )
