from django.db import models
import uuid

class Rfp(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256)
  due_date = models.DateField()
  subject = models.TextField()

  def __unicode__(self):
    return self.name