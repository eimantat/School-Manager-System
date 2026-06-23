from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name='نام')
    last_name = models.CharField(max_length=150, verbose_name='نام خانوادگی')

    national_code = models.CharField(
        max_length=10,
        null=True,
        verbose_name='کد ملی'
    )

    phone_number = models.CharField(
        max_length=20,
        null=True,
        verbose_name='شماره موبایل'
    )

    father_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='نام پدر'
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='تاریخ تولد'
    )

    address = models.TextField(
        blank=True,
        null=True,
        verbose_name='آدرس'
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='ایمیل'
    )
    GENDER_CHOICES = (
        ('M','مرد'),
        ('F','زن')
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name="جنسیت",null=True)
    
    
    


    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name or self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام نقش')
    code = models.CharField(max_length=50, unique=True, verbose_name='کد نقش')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نقش'
        verbose_name_plural = 'نقش‌ها'
        ordering = ['name']


class UserRole(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='user_roles',
        verbose_name='کاربر'
    )
    school = models.ForeignKey(
        'core.School',
        on_delete=models.CASCADE,
        related_name='user_roles',
        verbose_name='مدرسه'
    )
    academic_year = models.ForeignKey(
        'core.AcademicYear',
        on_delete=models.PROTECT,
        related_name='user_roles',
        verbose_name='سال تحصیلی'
    )
    role = models.ForeignKey(
        'users.Role',
        on_delete=models.PROTECT,
        related_name='user_roles',
        verbose_name='نقش'
    )
    start_date = models.DateField(verbose_name='تاریخ شروع مسئولیت')
    end_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان مسئولیت')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f'{self.user} - {self.role.name} - {self.school.name} - {self.academic_year.title}'

    class Meta:
        verbose_name = 'نقش کاربر'
        verbose_name_plural = 'نقش‌های کاربران'
        ordering = ['-start_date']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'school', 'academic_year', 'role', 'start_date'],
                name='uniq_user_school_year_role_start'
            )
        ]
