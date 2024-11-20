from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from accounts.models import User

from django.core.exceptions import ValidationError


def validate_mp3_file(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError('فقط فایل‌های MP3 قابل قبول هستند.')


# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.ImageField(upload_to='authors', verbose_name='تصویر')
    bio = models.TextField(verbose_name='بیوگرافی')
    instagram = models.CharField(max_length=255, blank=True, null=True, verbose_name='اینستاگرام')
    telegram = models.CharField(max_length=255, blank=True, null=True, verbose_name='تلگرام')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    color = models.CharField(max_length=7, default='#007bff', verbose_name='کد رنگ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='posts', blank=True, null=True, verbose_name='تصویر')  # اختیاری
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='دسته بندی')  # اختیاری
    short_description = models.TextField(blank=True, null=True, verbose_name='توضیح کوتاه')  # اختیاری
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')  # اختیاری
    content = RichTextField(blank=True, null=True, verbose_name='محتوا')  # اختیاری
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL,
                               verbose_name='نویسنده')  # اختیاری
    podcast = models.FileField(upload_to='podcasts', blank=True, null=True, verbose_name='پادکست',
                               validators=[validate_mp3_file])

    tags = models.ManyToManyField(Tag, blank=True, verbose_name='برچسب ها')  # اختیاری

    is_special = models.BooleanField(default=False, verbose_name='ویژه')
    is_urgent = models.BooleanField(default=False, verbose_name='فوری')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    released_at = models.DateTimeField(blank=True, null=True, verbose_name='زمان انتشار')  # اختیاری

    is_published = models.BooleanField(default=False, verbose_name='منتشر شده')  # وضعیت انتشار

    def save(self, *args, **kwargs):
        # auto slugify
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def is_complete(self):
        """بررسی می‌کند که آیا تمام فیلدهای ضروری تکمیل شده‌اند."""
        required_fields = [self.title, self.image, self.category, self.short_description, self.description,
                           self.content, self.author, self.released_at]
        return all(required_fields)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
