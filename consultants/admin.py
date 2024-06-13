from django.contrib import admin
from .models import Skill, Expert

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level']

class ExpertAdmin(admin.ModelAdmin):
    list_display = ['get_user_email', 'get_is_expert', 'start_date']
   
    def get_user_email(self, obj):
        return obj.user.name  # Assuming name is the field you use for username

    def get_is_expert(self, obj):
        return obj.user.is_expert

    get_user_email.short_description = 'User Email'
    get_is_expert.short_description = 'Is Expert'


admin.site.register(Skill, SkillAdmin)
admin.site.register(Expert, ExpertAdmin)