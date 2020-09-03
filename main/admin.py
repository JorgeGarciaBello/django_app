from django.contrib import admin
from .models import Tutorial
from django.db import models
from tinymce.widgets import TinyMCE 
# Register your models here.

class  TutorilAdmin(admin.ModelAdmin):
	fieldsets = [
	("Title/dat",{"fields":["tutorial_title","tutorial_published"]}),
	("Content",{"fields":["tutorial_content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(Tutorial,TutorilAdmin)