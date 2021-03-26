from django.db import models
# from Auth.models import Customer

# Create your models here.

class Booking(models.Model):
    cid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='cid')
    bid = models.AutoField(primary_key=True)
    spid = models.ForeignKey('Serviceprovider', models.DO_NOTHING, db_column='spid', blank=True, null=True)
    timing = models.IntegerField()
    category = models.CharField(max_length=5)
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'booking'

class Serviceprovider(models.Model):
    spid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5)
    address = models.CharField(max_length=75)
    sp_name = models.CharField(max_length=75)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'serviceprovider'

class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    c_name = models.CharField(max_length=75)
    contact_no = models.CharField(max_length=11)
    loggedin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'

class Bookedfor(models.Model):
    bid = models.ForeignKey('Booking', models.DO_NOTHING, db_column='bid')
    sid = models.OneToOneField('Service', models.DO_NOTHING, db_column='sid', primary_key=True)

    class Meta:
        managed = True
        db_table = 'bookedfor'
        unique_together = (('sid', 'bid'),)

class Service(models.Model):
    sid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5)
    dscrptn = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service'

