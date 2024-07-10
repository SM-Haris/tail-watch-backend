import uuid
from django.db import models
from history.utils import get_location_from_coordinates
from tags.models import Tag

class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    address = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.address = get_location_from_coordinates(self.latitude, self.longitude)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"History for Tag {self.tag.id} at {self.created_at}"