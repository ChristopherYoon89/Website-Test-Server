from django.contrib import admin
from .models import (
	Post, 
	ReleaseNotes, 
	ContactRequest, 
	NewsletterRequest,
    NewsletterUnsubscribeRequest,
	JobPost,
    JobApplication,
    Solution,
    Resource,
)
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }


admin.site.register(ReleaseNotes, BlogAdmin)
admin.site.register(Post, BlogAdmin)
admin.site.register(Solution, BlogAdmin)
admin.site.register(ContactRequest)
admin.site.register(NewsletterRequest)
admin.site.register(JobPost, BlogAdmin)
admin.site.register(JobApplication)
admin.site.register(NewsletterUnsubscribeRequest)
admin.site.register(Resource)