from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    c_name = models.CharField(max_length=75)
    contact_no = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'customer'
