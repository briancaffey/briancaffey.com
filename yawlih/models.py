from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Company(models.Model):
    name_en = models.CharField(max_length=400, blank=True, null=True)
    name_cn = models.CharField(max_length=400, blank=True, null=True)
    website = models.URLField(max_length=500)
    intro_en = models.TextField(blank=True, null=True)
    intro_cn = models.TextField(blank=True, null=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-name_en']

    def __str__(self):
        return str(self.name_en)

    def total_jobs(self):
        jobs = len(Job.objects.filter(company=self.id))
        return jobs

    def jobs(self):
        jobs = Job.objects.filter(company=self.id)
        return jobs

    def total_news(self):
        news = len(News.objects.filter(company=self.id))
        return news

    def news(self):
        news = News.objects.filter(company=self.id)
        return news

    def investments(self):
        investments = Investment.objects.filter(company=self.id)
        return investments


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position_cn = models.CharField(max_length=300)
    position_en = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    link = models.URLField(max_length=1000, default='')
    post_date = models.DateField()
    monthly_salary_rmb = models.DecimalField(max_digits=10,decimal_places=0)
    tags = TaggableManager()

    class Meta:
        ordering = ['-monthly_salary_rmb']

    def __str__(self):
        return str(self.position_en)

class News(models.Model):
    company = models.ForeignKey(Company)
    headline = models.CharField(max_length=500, default='')
    text = models.TextField(default='')
    publish_date = models.DateField()
    news_outlet = models.CharField(max_length=100)
    tags = TaggableManager()
    link = models.URLField(max_length=1000, default='')

    def __str__(self):
        return str(self.headline)


class Investor(models.Model):
    name_en = models.CharField(max_length=300)
    name_cn = models.CharField(max_length=300)
    website = models.URLField(max_length=500)
    intro_en = models.TextField(blank=True, null=True)
    intro_cn = models.TextField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return str(self.name_en)

class Investment(models.Model):
    round_type = models.CharField(max_length=500)
    amount_rmb = models.DecimalField(max_digits=10,decimal_places=0)
    investors = models.ManyToManyField(Investor, blank=True)
    company = models.ForeignKey(Company)
    headline = models.CharField(max_length=500, default='')
    text = models.TextField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)



    def __str__(self):
        return str(self.company.name_en) + " - " + str(self.round_type)
