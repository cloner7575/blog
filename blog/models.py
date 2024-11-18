from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from accounts.models import User


# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.ImageField(upload_to='authors', verbose_name='تصویر')
    bio = models.TextField(verbose_name='بیوگرافی')

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
    image = models.ImageField(upload_to='posts', verbose_name='تصویر')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    short_description = models.TextField(verbose_name='توضیح کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    content = RichTextField(verbose_name='محتوا')
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده')
    time_to_read = models.IntegerField(default=3, verbose_name='زمان مطالعه بر حسب دقیقه')
    tags = models.ManyToManyField(Tag, verbose_name='برچسب ها')

    is_special = models.BooleanField(default=False, verbose_name='ویژه')
    is_urgent = models.BooleanField(default=False, verbose_name='فوری')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    released_at = models.DateTimeField(verbose_name='زمان انتشار')

    def save(self, *args, **kwargs):
        # auto slugify
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
