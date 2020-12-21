from django.db import models
from django.contrib.auth import get_user_model

class Blog(models.Model):
  country_name = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  owner = models.ForeignKey(
      get_user_model(),
      related_name='blogs',
      on_delete=models.CASCADE,
  )

  def __str__(self):
    return f"I visited '{self.country_name}'. {self.description}."

  def as_dict(self):
    return {
        'id': self.id,
        'country_name': self.country_name,
        'description': self.description,
    }
