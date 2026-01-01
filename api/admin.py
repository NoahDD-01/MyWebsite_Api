from django.contrib import admin
from django.utils.html import format_html

from .models import ServiceText,ServiceBox,ProjectBox,Profile,ContactUs

# Register your models here.
@admin.register(ServiceText)
class ServiceTextAdmin(admin.ModelAdmin):
    list_display = ['service_text_en','service_text_mm','created_at']
    list_filter = ['created_at']

@admin.register(ServiceBox)
class ServiceBoxAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_mm','image_tag','created_at']
    list_filter = ['created_at']

    # image preview
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'ServiceImage'

@admin.register(ProjectBox)
class ProjectBoxAdmin(admin.ModelAdmin):
    list_display = ['project_title','project_des','project_link']
    list_filter = ['created_at']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_title','image_tag']
    list_filter = ['created_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'ProfileImage'

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'message', 'created_at']
    # နောက်ဆုံးမှာ comma (,) ပါတာ သေချာပါစေ (Tuple ဖြစ်သွားအောင်လို့ပါ)
    ordering = ('-created_at',)
    search_fields = ('name', 'phone_number',)
    list_filter = ('created_at',)