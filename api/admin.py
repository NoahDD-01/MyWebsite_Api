from django.contrib import admin
from django.utils.html import format_html

from .models import ( ServiceText,ServiceBox,ProjectBox,Profile,ContactUs,AboutUs,OurMission,ChooseUs)

# Register your models here.
@admin.register(ServiceText)
class ServiceTextAdmin(admin.ModelAdmin):
    list_display = ['service_text_en','service_text_mm','created_at']
    list_filter = ['created_at']
    ordering =  ['created_at']


@admin.register(ServiceBox)
class ServiceBoxAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_mm', 'image_tag', 'created_at']
    list_filter = ['created_at']
    ordering =  ['created_at']

    def image_tag(self, obj):
        if obj.icon:
            # .format() ကို ဖြုတ်ပြီး အခုလို ရေးရပါမယ်
            return format_html('<img src="{}" width="100" height="auto" style="border-radius: 8px;" />', obj.icon.url)
        return "-"
    
    image_tag.short_description = 'Service Icon'

@admin.register(ProjectBox)
class ProjectBoxAdmin(admin.ModelAdmin):
    list_display = ['project_num', 'project_title_en', 'project_title_mm', 'project_link', 'created_at']

    list_filter = ['created_at']
    
    ordering = ['project_num']
    
    search_fields = ('project_title_en', 'project_title_mm')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_title_en', 'profile_title_mm', 'image_tag', 'updated_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:5px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Profile Image'

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'message', 'created_at']
    ordering = ('-created_at',)
    search_fields = ('name', 'phone_number',)
    list_filter = ('created_at',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['des_en','des_mm','created_at']
    ordering = ('-created_at',)

@admin.register(OurMission)
class OurMissionAdmin(admin.ModelAdmin):
    list_display = ['des_en','des_mm','created_at']
    ordering = ('-created_at',)

@admin.register(ChooseUs)
class ChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_mm','des_en','des_mm','created_at']
    ordering = ('-created_at',)
