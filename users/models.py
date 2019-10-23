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

class DataCheck(models.Model):
    old_bsj_pact = models.CharField('bsjpact_data',max_length=556)
    old_bb_pact = models.CharField('bbpact_data',max_length=556)
    old_v3_pact = models.CharField('v3pact_data',max_length=566)
    new_bsj_pact=models.CharField('bsjpact_data', max_length=556)
    new_bb_pact=models.CharField('bbpact_data', max_length=556)
    new_v3_pact=models.CharField('v3pact_data', max_length=566)

    class Meta:
        verbose_name='校验'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.old_bsj_pact