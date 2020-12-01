from django.db import models

from NhomHangHoa.models import Nhomhanghoa

# Create your models here.

class Hanghoa(models.Model):
    mahh = models.AutoField(db_column='MaHH', primary_key=True)
    ten = models.CharField(db_column='Ten', max_length=100)
    hinhanh = models.FileField(db_column='HinhAnh', blank=True, null=True) #max_length=200,
    mota = models.CharField(db_column='MoTa', max_length=1000, blank=True, null=True)
    gia = models.DecimalField(db_column='Gia', max_digits=10, decimal_places=0)
    soluong = models.IntegerField(db_column='SoLuong', blank=True, null=True)
    manhom = models.ForeignKey('NhomHangHoa.Nhomhanghoa', models.DO_NOTHING, db_column='MaNhom')


    class Meta:
        managed = False
        db_table = 'hanghoa'


    def __str__(self):
        return self.ten
    