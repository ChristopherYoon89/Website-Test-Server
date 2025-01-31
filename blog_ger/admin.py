from django.contrib import admin
from .models import (
	PostGerman,
	ReleaseNotesGerman,
	JobPostGerman,
  SolutionGerman,
  JobApplicationGerman,
)
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }
    

admin.site.register(PostGerman, BlogAdmin)
admin.site.register(ReleaseNotesGerman, BlogAdmin)
admin.site.register(JobPostGerman, BlogAdmin)
admin.site.register(SolutionGerman, BlogAdmin)
admin.site.register(JobApplicationGerman)
