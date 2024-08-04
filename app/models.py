from django.db import models

# Create your models here.
class Table1(models.Model):
    id = models.IntegerField(primary_key=True)
    Init = models.CharField(max_length=50)
    GIP = models.CharField(max_length=50)
    Comment_GIP = models.CharField(max_length=50)
    initiator = models.DateField()
    class Meta:
        db_table = 'Table_1'
        managed = False