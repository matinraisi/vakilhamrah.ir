from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.
class profileInline(admin.TabularInline):  # یا از StackedInline استفاده کنید
    model = Profile
    extra = 1  # تعداد فیلدهای خالی برای افزودن رکورد جدید

admin.site.unregister(User)  # حذف ثبت پیش‌فرض User
@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [profileInline]