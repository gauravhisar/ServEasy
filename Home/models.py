from django.db import models

# Create your models here.

service_to_category = {'electricians':'EL', 'carpenters' : 'CA', 'salonForMen':'SM', 'plumbers': 'PL', 'BeauticiansForWomen' : 'BW'}
category_to_service = {'EL':'electricians',  'CA':'carpenters' , 'SM':'salonForMen',  'PL':'plumbers',  'BW':'BeauticiansForWomen' }
loggedin_userid = False

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
    
class Booking(models.Model):
    cid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='cid')
    bid = models.AutoField(primary_key=True)
    spid = models.ForeignKey('Serviceprovider', models.DO_NOTHING, db_column='spid', blank=True, null=True)
    timing = models.IntegerField()
    category = models.CharField(max_length=5)
    status = models.CharField(max_length=1)
    bdate = models.DateField()
    amount = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'booking'

class Service(models.Model):
    sid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5)
    dscrptn = models.CharField(max_length=300, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        managed = True
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
        managed = True
        db_table = 'serviceprovider'

class Bookedfor(models.Model):
    bid = models.ForeignKey('Booking', models.DO_NOTHING, db_column='bid')
    sid = models.OneToOneField('Service', models.DO_NOTHING, db_column='sid')

    class Meta:
        managed = True
        db_table = 'bookedfor'
        unique_together = (('sid', 'bid'),)