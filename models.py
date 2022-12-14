# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CapstoneAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    question = models.ForeignKey('CapstoneQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'capstone_answer'


class CapstoneQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'capstone_question'


class CommonCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'common_customuser'


class CommonUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    semester = models.CharField(max_length=100)
    lastgpa = models.CharField(max_length=50)
    fullgpa = models.CharField(max_length=200)
    income = models.CharField(max_length=200)
    departments = models.CharField(max_length=200)
    residence = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'common_user'


class CommonUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CommonUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'common_user_groups'
        unique_together = (('user', 'group'),)


class CommonUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CommonUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'common_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CommonCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Scholar(models.Model):
    semester = models.CharField(max_length=20, blank=True, null=True)
    lastgpa = models.FloatField(blank=True, null=True)
    fullgpa = models.FloatField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    residence = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholar'


class Wholescholar(models.Model):
    number = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    attachment_url = models.TextField(blank=True, null=True)
    attachment_content = models.TextField(blank=True, null=True)
    current_url = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wholescholar'
