from django.contrib import admin
from .models import (
    SkillCategory,
    Skill,
    UserSkill,
    OrganizationType,
    Organization,
    OrganizationPosition,
    OrganizationMembership,
    AchievementCategory,
    AchievementType,
    AchievementLevel,
    AchievementRank,
    UserAchievement,
)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "code")
    list_filter = ("category",)
    search_fields = ("name", "code")


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ("user", "skill", "level", "academic_year", "is_pre_school")
    list_filter = ("skill", "academic_year", "is_pre_school")
    search_fields = ("user__first_name", "user__last_name", "skill__name")


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "organization_type", "academic_year", "is_active")
    list_filter = ("organization_type", "school", "academic_year", "is_active")
    search_fields = ("name",)


@admin.register(OrganizationPosition)
class OrganizationPositionAdmin(admin.ModelAdmin):
    list_display = ("title", "organization_type", "code")
    list_filter = ("organization_type",)
    search_fields = ("title", "code")


@admin.register(OrganizationMembership)
class OrganizationMembershipAdmin(admin.ModelAdmin):
    list_display = ("user_role", "organization", "position", "start_date", "end_date", "is_active")
    list_filter = ("organization", "position", "is_active")
    search_fields = ("user_role__user__first_name", "user_role__user__last_name", "organization__name")


@admin.register(AchievementCategory)
class AchievementCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(AchievementType)
class AchievementTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "code")
    list_filter = ("category",)
    search_fields = ("name", "code")


@admin.register(AchievementLevel)
class AchievementLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(AchievementRank)
class AchievementRankAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "achievement_type", "level", "rank", "school", "event_date")
    list_filter = ("achievement_type", "level", "rank", "school", "academic_year")
    search_fields = ("user__first_name", "user__last_name", "title")
