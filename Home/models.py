from django.db import models

# Create your models here.

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