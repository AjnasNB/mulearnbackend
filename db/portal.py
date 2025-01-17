from django.db import models

from .user import User


class Portal(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    portal_key = models.CharField(max_length=36)
    name = models.CharField(max_length=75)
    link = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='updated_by',
                                   related_name='portal_updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',
                                   related_name='portal_created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'portal'


class PortalUserAuth(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_authenticated = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',
                                   related_name='portal_user_auth_created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'portal_user_auth'


class PortalUserMailValidate(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=36)
    expiry = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',
                                   related_name='portal_user_mail_validate_created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'portal_user_mail_validate'
