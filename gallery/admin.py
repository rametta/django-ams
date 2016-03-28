from django.contrib import admin
from gallery.models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'artist',)

admin.site.register(Work, WorkAdmin)

admin.site.site_header = 'Gallery X Art System'
admin.site.site_title = 'Gallery X'