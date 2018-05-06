import re
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Count
# Create your models here.
POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)

class PostManager(models.Manager):
    def filter_by_tags(self, tag_list=[], count=10):
        qs = self.all()
        for tag in tag_list:
            qs = qs.filter(tags__name=tag)
        if count:
            qs = qs[:count]
        return qs

class Post(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    banner_photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag",related_name="tags")
    status = models.CharField(max_length=9, choices=POST_STATUS, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.title)
    objects = PostManager()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True) 
    author = models.CharField(max_length=150)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.text)

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)



class TagManager(models.Manager):
    def most_popular(self, count=5):
        return self.annotate(num_posts=Count("post"))
        order_by("-num_posts")[:count]

tag_pattern = re.compile(r'^w+$')
def validate_tag_name(name):
    if not tag_pattern.search(name):
        raise ValidationError("not a valid tag name")

class Tag(models.Model):
    name = models.CharField(max_length=20, validators=[validate_tag_name])
    objects = TagManager()

    def __unicode__(self):
        return self.name

