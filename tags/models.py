from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Tag(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    tag = models.CharField(max_length=50)


    def create_slug(instance):
        slug = slugify(instance.tag)
        return slug


    def get_items(self):
        ct = ContentType.objects.get_for_model('readingmaterial')
        items = ct.filter(tag=self.slug)
        return items

    def __str__(self):
        return str(self.tag)
