from django.contrib import admin
from gallery.models import Work, Upload

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'artist',)
    
class UploadAdmin(admin.ModelAdmin):
    list_display = ('work', 'image')
    list_display_links = ('work',)

admin.site.register(Work, WorkAdmin)
admin.site.register(Upload, UploadAdmin)

admin.site.site_header = 'Gallery X Art System'
admin.site.site_title = 'Gallery X'