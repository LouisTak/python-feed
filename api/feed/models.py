from django.db import models
from django.conf import settings

# Create your models here.
class Feed(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feeds')

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'feeds'