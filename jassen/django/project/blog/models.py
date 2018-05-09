import re
from django.core.exceptions import ValidationError
from django.db import models
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage
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
    banner_photo = VersatileImageField(
        'Image',
        upload_to='static/media'
 )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag",related_name="tags")
    status = models.CharField(max_length=9, choices=POST_STATUS, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.title)
    objects = PostManager()


    def tag_list(self):
        qs = self.tags.values_list("title", flat=True)
        if qs:
            return ", ".join(qs)
        else:
            return ""

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

tag_pattern = re.compile(r'^[\w.@ +-]+$',)
def validate_tag_name(title):
    if not tag_pattern.search(title):
        raise ValidationError("not a valid tag title")

class Tag(models.Model):
    title = models.CharField(max_length=20, validators=[validate_tag_name])
    objects = TagManager()

    def __str__(self):
        return '{}'.format(self.title)

