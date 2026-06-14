from django.db import models


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "دسته‌بندی مهارت"
        verbose_name_plural = "دسته‌بندی مهارت‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.PROTECT,
        related_name="skills"
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="skills"
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        related_name="user_skills"
    )
    level = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    academic_year = models.ForeignKey(
        "core.AcademicYear",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="user_skills"
    )
    is_pre_school = models.BooleanField(default=False)

    class Meta:
        verbose_name = "مهارت کاربر"
        verbose_name_plural = "مهارت‌های کاربران"
        ordering = ["user", "skill"]
        unique_together = ("user", "skill", "academic_year", "is_pre_school")

    def __str__(self):
        return f"{self.user} - {self.skill}"


class OrganizationType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "نوع تشکل"
        verbose_name_plural = "انواع تشکل"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Organization(models.Model):
    school = models.ForeignKey(
        "core.School",
        on_delete=models.CASCADE,
        related_name="organizations"
    )
    organization_type = models.ForeignKey(
        OrganizationType,
        on_delete=models.PROTECT,
        related_name="organizations"
    )
    name = models.CharField(max_length=150)
    academic_year = models.ForeignKey(
        "core.AcademicYear",
        on_delete=models.PROTECT,
        related_name="organizations"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "تشکل"
        verbose_name_plural = "تشکل‌ها"
        ordering = ["school", "name"]

    def __str__(self):
        return self.name


class OrganizationPosition(models.Model):
    organization_type = models.ForeignKey(
        OrganizationType,
        on_delete=models.CASCADE,
        related_name="positions"
    )
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "سمت تشکل"
        verbose_name_plural = "سمت‌های تشکل"
        ordering = ["organization_type", "title"]
        unique_together = ("organization_type", "code")

    def __str__(self):
        return self.title


class OrganizationMembership(models.Model):
    user_role = models.ForeignKey(
        "users.UserRole",
        on_delete=models.CASCADE,
        related_name="organization_memberships"
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    position = models.ForeignKey(
        OrganizationPosition,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="memberships"
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "عضویت در تشکل"
        verbose_name_plural = "عضویت‌ها در تشکل"
        ordering = ["organization", "user_role"]
        unique_together = ("user_role", "organization", "position")

    def __str__(self):
        return f"{self.user_role} - {self.organization}"


class AchievementCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "دسته‌بندی افتخار"
        verbose_name_plural = "دسته‌بندی افتخارات"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AchievementType(models.Model):
    category = models.ForeignKey(
        AchievementCategory,
        on_delete=models.PROTECT,
        related_name="types"
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "نوع افتخار"
        verbose_name_plural = "انواع افتخار"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class AchievementLevel(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "سطح افتخار"
        verbose_name_plural = "سطوح افتخار"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AchievementRank(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "رتبه افتخار"
        verbose_name_plural = "رتبه‌های افتخار"
        ordering = ["name"]

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="achievements"
    )
    achievement_type = models.ForeignKey(
        AchievementType,
        on_delete=models.PROTECT,
        related_name="user_achievements"
    )
    level = models.ForeignKey(
        AchievementLevel,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="user_achievements"
    )
    rank = models.ForeignKey(
        AchievementRank,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="user_achievements"
    )
    school = models.ForeignKey(
        "core.School",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_achievements"
    )
    academic_year = models.ForeignKey(
        "core.AcademicYear",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="user_achievements"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    is_pre_school = models.BooleanField(default=False)

    class Meta:
        verbose_name = "افتخار کاربر"
        verbose_name_plural = "افتخارات کاربران"
        ordering = ["-event_date", "user"]

    def __str__(self):
        return f"{self.user} - {self.title}"
