from django.db import models

# Create your models here.

class Nhomhanghoa(models.Model):
    manhom = models.AutoField(db_column='MaNhom', primary_key=True)
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nhomhanghoa'

    def __str__(self):
        return self.ten