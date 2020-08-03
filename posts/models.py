from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField('URL', max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(help_text="Agrrrhhhh. Just text. Comeon, write something")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Group", related_name="posts",)

    def __str__(self):
        return self.text[0:100]
