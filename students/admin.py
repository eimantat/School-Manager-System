from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        
        "mother_name",
        "father_status",
        "mother_status",
    )

    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__national_code",
        "mother_name",
    )

    list_filter = (
        
        "father_status",
        "mother_status",
    )

    autocomplete_fields = ("user",)

    fieldsets = (
        ("اطلاعات کاربر", {
            "fields": ("user",)
        }),

        ("اطلاعات فردی", {
            "fields": (
                
                "mother_name",
            )
        }),

        ("وضعیت والدین", {
            "fields": (
                "father_status",
                "mother_status",
            )
        }),

        ("اطلاعات تکمیلی", {
            "fields": (
                "guardian_notes",
            )
        }),
    )
