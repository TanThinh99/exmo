from django.db import models

from TaiKhoan.models import Taikhoan

# Create your models here.

class Donhang(models.Model):
    madh = models.AutoField(db_column='MaDH', primary_key=True)
    thoigiandathang = models.DateTimeField(db_column='ThoiGianDatHang', auto_now_add=True)
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True, default=0)
    manv = models.ForeignKey('TaiKhoan.Taikhoan', models.DO_NOTHING, db_column='MaNV', related_name='manv')
    makh = models.ForeignKey('TaiKhoan.Taikhoan', models.DO_NOTHING, db_column='MaKH', related_name='makh')

    class Meta:
        managed = False
        db_table = 'donhang'
        
    def __str__(self):
        return str(self.madh)