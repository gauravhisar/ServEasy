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


class AuthUser(models.Model):
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

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bookedfor(models.Model):
    bid = models.ForeignKey('Booking', models.DO_NOTHING, db_column='bid')
    sid = models.OneToOneField('Service', models.DO_NOTHING, db_column='sid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'bookedfor'
        unique_together = (('sid', 'bid'),)


class Booking(models.Model):
    cid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='cid')
    bid = models.AutoField(primary_key=True)
    spid = models.ForeignKey('Serviceprovider', models.DO_NOTHING, db_column='spid', blank=True, null=True)
    timing = models.IntegerField()
    category = models.CharField(max_length=5)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'booking'


class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    c_name = models.CharField(max_length=75)
    contact_no = models.CharField(max_length=11)
    loggedin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Provides(models.Model):
    sid = models.OneToOneField('Service', models.DO_NOTHING, db_column='sid', primary_key=True)
    spid = models.ForeignKey('Serviceprovider', models.DO_NOTHING, db_column='spid')

    class Meta:
        managed = False
        db_table = 'provides'
        unique_together = (('sid', 'spid'),)


class Service(models.Model):
    sid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5)
    dscrptn = models.CharField(max_length=300, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service'


class Serviceprovider(models.Model):
    spid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5)
    address = models.CharField(max_length=75)
    sp_name = models.CharField(max_length=75)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'serviceprovider'
