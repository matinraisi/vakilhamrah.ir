from django.contrib import admin
from .models import *
from Authentication.models import *
# Register your models here.

class QaAInline(admin.TabularInline):  # یا از StackedInline استفاده کنید
    model = QaA
    extra = 1  # تعداد فیلدهای خالی برای افزودن رکورد جدید

class BillReqInline(admin.TabularInline):  # یا از StackedInline استفاده کنید
    model = BillRequest
    extra = 1  # تعداد فیلدهای خالی برای افزودن رکورد جدید

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [QaAInline,BillReqInline]
    list_display = ('user', 'is_lawyer')  # فیلدهایی که می‌خواهید در لیست نمایش داده شوند

admin.site.register(BillRequest)
admin.site.register(QaA)
admin.site.register(News)
admin.site.register(LegalFiles)
admin.site.register(LegalCategory)
admin.site.register(Lawyer)
admin.site.register(LawyerType)


