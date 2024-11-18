from symtable import Class

from django.db import models


# Create your models here.

class SocialMedia(models.Model):
    telegram_channel = models.CharField(max_length=255, verbose_name='کانال تلگرام')
    telegram_member = models.IntegerField(verbose_name='تعداد اعضای کانال')

    instagram_page = models.CharField(max_length=255, verbose_name='صفحه اینستاگرام')
    instagram_follower = models.IntegerField(verbose_name='تعداد فالوور های صفحه')

    # single instance
    def save(self, *args, **kwargs):
        # if exists, update
        if SocialMedia.objects.exists():
            self.pk = SocialMedia.objects.first().pk
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'رسانه های اجتماعی'
        verbose_name_plural = 'رسانه های اجتماعی'


