from django.db import models
from django.utils.safestring import mark_safe


class List(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.TextField()
    Image = models.FileField(null="true", blank="false")

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % (self.Image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

