from django.db import models
from datetime import datetime
from django.utils import timezone

class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Categories"

	def _str_(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_description = models.CharField(max_length=200)
	tutorial_type = models.CharField(max_length=200)




# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=timezone.now())

	def __str__(self):
		return self.tutorial_title