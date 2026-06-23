from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from jalali_date.admin import ModelAdminJalaliMixin, TabularInlineJalaliMixin
from .models import User, Role, UserRole

# ۱. اینلاین برای نقش‌های کاربر
class UserRoleInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = UserRole
    extra = 1
    # نکته: autocomplete_fields را فعلاً برداشتم تا اگر در core/admin تنظیم نشده باشد، ارور ندهد
    verbose_name = "نقش و انتساب کاربر"
    verbose_name_plural = "نقش‌ها و انتساب‌های کاربر"

# ۲. ادمین اصلی کاربر
@admin.register(User)
class CustomUserAdmin(ModelAdminJalaliMixin, UserAdmin):
    inlines = [UserRoleInline]
    
    list_display = ("username", "first_name", "last_name", "national_code", "is_active")
    search_fields = ("username", "first_name", "last_name", "national_code")
    
    # فیلدبندی صفحه ویرایش
    fieldsets = (
        ("اطلاعات ورود", {"fields": ("username", "password")}),
        ("اطلاعات فردی", {"fields": ("first_name", "last_name", "national_code", "father_name", "gender", "birth_date")}),
        ("ارتباطات", {"fields": ("phone_number", "email", "address")}),
        ("دسترسی‌های سیستمی", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("تاریخ‌های مهم", {"fields": ("last_login", "date_joined")}),
    )

    # فیلدبندی صفحه «ساخت کاربر جدید»
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1","password2", "first_name", "last_name", "national_code", "gender"),
        }),
    )

    # --- این متد باید حتماً داخل کلاس باشد (با رعایت فاصله از لبه) ---
    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []  # در صفحه Add User اینلاین را نشان نده
        return super().get_inline_instances(request, obj)
    # ---------------------------------------------------------

# ۳. ادمین مدیریت نقش‌ها
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')
