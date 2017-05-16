from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.



class Project(models.Model):

	name = models.CharField(max_length=500)
	slug = models.SlugField(unique=True, default="")
	emoji = models.CharField(max_length=50, default="")
	link = models.URLField(null=True, blank=True)
	description = models.CharField(max_length=10000)
	full_description = models.CharField(max_length=10000, default="")
	order = models.PositiveIntegerField(default=0)
	name = models.CharField(max_length=500)
	tags = TaggableManager()

	def __str__(self):
		return str(self.name)

	def detail_url(self):
		return "/projects/" + self.slug

def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Project.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" % (slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Project)
