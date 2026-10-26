from django.contrib import admin
from .models import Note
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display=['title','topic','state','published_at','updated_at']
    list_filter=['state','topic']
    search_fields=['title','summary','body']
    prepopulated_fields={'slug':('title',)}
    readonly_fields=['updated_at']
admin.site.site_header='Technical Journal · Redazione'
admin.site.site_title='Technical Journal'
