from django.db import models

# Create your models here.

service_to_category = {'electricians':'EL', 'carpenters' : 'CA', 'salonForMen':'SM', 'plumbers': 'PL', 'BeauticiansForWomen' : 'BW'}
category_to_service = {'EL':'electricians',  'CA':'carpenters' , 'SM':'salonForMen',  'PL':'plumbers',  'BW':'BeauticiansForWomen' }
class Service(models.Model):
    sid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=5)
    dscrptn = models.CharField(max_length=300, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'service'