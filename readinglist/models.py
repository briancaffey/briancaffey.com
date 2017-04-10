from django.db import models
from django.conf import settings
# Create your models here.
from tags.models import Tag
from comments.models import Comment #users can comment on reading list
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save, post_save



class ReadingMaterial(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=400, unique=True)
    tags = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-pk']

    def get_tags(self):

        tags = Tag.objects.filter(object_id=self.id)
        return tags



def post_save_readingmaterial_receiver(sender, instance, *args, **kwargs):
    if instance.tags:
        unique_tags = list(set(instance.tags.split(' ')))
        ct = ContentType.objects.get_for_model(instance)
        for tag in unique_tags:
            print("Instance" + str(instance.pk))
            Tag.objects.create(tag=tag, object_id=instance.id, content_type=ct)

#
# def post_save_readingmaterial_receiver(sender, insance, *args, **kwargs):
#     Tag.objects.create(tag=tag, object_id=instance.id, content_type=ct)
#
#
post_save.connect(post_save_readingmaterial_receiver, sender=ReadingMaterial)
