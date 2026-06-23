from django.db import models
from django.conf import settings


class StudentProfile(models.Model):

    
    class ParentStatus(models.TextChoices):
        ALIVE = "alive", "در قید حیات"
        DEAD = "dead", "فوت شده"
        DIVORCED = "divorced", "متارکه"
        OTHER = "other", "سایر"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
        verbose_name="کاربر"
    )

    

    mother_name = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name="نام مادر"
    )

    father_status = models.CharField(
        max_length=10,
        choices=ParentStatus.choices,
        default=ParentStatus.ALIVE,
        verbose_name="وضعیت پدر"
    )

    mother_status = models.CharField(
        max_length=10,
        choices=ParentStatus.choices,
        default=ParentStatus.ALIVE,
        verbose_name="وضعیت مادر"
    )

    guardian_notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات سرپرست"
    )
    health_condition = models.BooleanField(
        max_length=1,
        default=True,
        unique=True
    )

    medical_notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="بیماری خاص"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "پروفایل دانش‌آموز"
        verbose_name_plural = "پروفایل دانش‌آموزان"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
