from django.db import models


class Note(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "note"
    verbose_name_plural = "notes"



