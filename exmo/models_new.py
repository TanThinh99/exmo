# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chitietdonhang(models.Model):
    mahh = models.ForeignKey('Hanghoa', models.DO_NOTHING, db_column='MaHH')  # Field name made lowercase.
    madh = models.ForeignKey('Donhang', models.DO_NOTHING, db_column='MaDH')  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong')  # Field name made lowercase.
    giadathang = models.DecimalField(db_column='GiaDatHang', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chitietdonhang'


class Donhang(models.Model):
    madh = models.AutoField(db_column='MaDH', primary_key=True)  # Field name made lowercase.
    thoigiandathang = models.DateTimeField(db_column='ThoiGianDatHang')  # Field name made lowercase.
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.
    manv = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='MaNV')  # Field name made lowercase.
    makh = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='MaKH')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'donhang'


class Hanghoa(models.Model):
    mahh = models.AutoField(db_column='MaHH', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100)  # Field name made lowercase.
    hinhanh = models.CharField(db_column='HinhAnh', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mota = models.CharField(db_column='MoTa', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    gia = models.DecimalField(db_column='Gia', max_digits=10, decimal_places=0)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong', blank=True, null=True)  # Field name made lowercase.
    manhom = models.ForeignKey('Nhomhanghoa', models.DO_NOTHING, db_column='MaNhom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hanghoa'


class Nhomhanghoa(models.Model):
    manhom = models.AutoField(db_column='MaNhom', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nhomhanghoa'


class Taikhoan(models.Model):
    matk = models.AutoField(db_column='MaTK', primary_key=True)  # Field name made lowercase.
    hoten = models.CharField(db_column='HoTen', max_length=70)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sodienthoai = models.CharField(db_column='SoDienThoai', max_length=15, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    isadmin = models.IntegerField(db_column='isAdmin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taikhoan'
