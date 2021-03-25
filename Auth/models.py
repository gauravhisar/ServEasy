from django.db import models

# Create your models here.

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