from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    telephone = models.CharField('Telephone',max_length=11,blank=True)
    org = models.CharField('Organization',max_length=50,blank=True)
    mod_date = models.DateTimeField('Last modified',auto_now=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user