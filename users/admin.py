from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, UserRole
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(User)
class CustomUserAdmin(ModelAdminJalaliMixin,UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "national_code",
        "phone_number",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "national_code",
        "phone_number",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )

    fieldsets = (
        ("اطلاعات ورود", {
            "fields": ("username", "password")
        }),
        ("اطلاعات شخصی", {
            "fields": (
                "first_name",
                "last_name",
                "national_code",
                "phone_number",
                "father_name",
                "birth_date",
                "email",
                "address",
                "gender",
                "mother_name",
                "father_status",
                "mother_status",
                "guardian_notes"
            )
        }),
        ("دسترسی‌ها", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("تاریخ‌ها", {
            "fields": ("last_login", "date_joined")
        }),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")
    search_fields = ("name", "code")
    list_filter = ("is_active",)


@admin.register(UserRole)
class UserRoleAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = (
        "user",
        "role",
        "school",
        "academic_year",
        "start_date",
        "end_date",
        "is_active",
    )

    list_filter = (
        "role",
        "school",
        "academic_year",
        "is_active",
    )

    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__national_code",
        "school__name",
    )

    autocomplete_fields = (
        "user",
        "school",
        "role",
        "academic_year",
    )
