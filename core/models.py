from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام شهر')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'
        ordering = ['name']


class District(models.Model):
    city = models.ForeignKey(
        'core.City',
        on_delete=models.CASCADE,
        related_name='districts',
        verbose_name='شهر'
    )
    name = models.CharField(max_length=100, verbose_name='نام منطقه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f'{self.city.name} - {self.name}'

    class Meta:
        verbose_name = 'منطقه'
        verbose_name_plural = 'مناطق'
        ordering = ['city__name', 'name']
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'name'],
                name='uniq_district_per_city'
            )
        ]


class EducationLevel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='مقطع تحصیلی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مقطع تحصیلی'
        verbose_name_plural = 'مقاطع تحصیلی'
        ordering = ['name']


class SchoolType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نوع مدرسه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نوع مدرسه'
        verbose_name_plural = 'انواع مدرسه'
        ordering = ['name']


class AcademicYear(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='عنوان سال تحصیلی')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سال تحصیلی'
        verbose_name_plural = 'سال‌های تحصیلی'
        ordering = ['-start_date']


class School(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام مدرسه')
    code = models.CharField(max_length=50, unique=True, verbose_name='کد مدرسه')
    district = models.ForeignKey(
        'core.District',
        on_delete=models.PROTECT,
        related_name='schools',
        verbose_name='منطقه'
    )
    education_level = models.ForeignKey(
        'core.EducationLevel',
        on_delete=models.PROTECT,
        related_name='schools',
        verbose_name='مقطع تحصیلی'
    )
    school_type = models.ForeignKey(
        'core.SchoolType',
        on_delete=models.PROTECT,
        related_name='schools',
        verbose_name='نوع مدرسه'
    )
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='شماره تماس')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مدرسه'
        verbose_name_plural = 'مدارس'
        ordering = ['name']
