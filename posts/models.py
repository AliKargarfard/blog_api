# posts/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("آخرین بروزرسانی"))

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    STATUS_CHOICES = [
        ('draft', _("پیش‌نویس")),
        ('published', _("منتشر شده")),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name=_("نویسنده"))
    title = models.CharField(max_length=200, verbose_name=_("عنوان"))
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name=_("اسلاگ"))
    content = models.TextField(verbose_name=_("محتوا"))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name=_("وضعیت"))
    publish = models.DateTimeField(null=True, blank=True, verbose_name=_("تاریخ انتشار"))

    class Meta:
        ordering = ['-publish']
        verbose_name = _("پست")
        verbose_name_plural = _("پست‌ها")

    def __str__(self):
        return self.title
