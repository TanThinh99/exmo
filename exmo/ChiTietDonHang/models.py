from django.db import models

from HangHoa.models import Hanghoa
from DonHang.models import Donhang

# Create your models here.

class Chitietdonhang(models.Model):
    machitiet = models.AutoField(db_column='MaChiTiet', primary_key=True)
    mahh = models.ForeignKey('HangHoa.Hanghoa', models.DO_NOTHING, db_column='MaHH')
    madh = models.ForeignKey('DonHang.Donhang', models.DO_NOTHING, db_column='MaDH')
    soluong = models.IntegerField(db_column='SoLuong')
    giadathang = models.DecimalField(db_column='GiaDatHang', max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chitietdonhang'

    def __str__(self):
        return "Ten hang: "+ str(self.mahh) +", Ma don hang: "+ str(self.madh)