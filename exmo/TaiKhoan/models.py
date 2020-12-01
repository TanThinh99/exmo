from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, isadmin=1):
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            username = username
        )
        user.set_password(password)
        user.isadmin = 0

        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            isadmin=0
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            isadmin=1
        )
        return user


class Taikhoan(AbstractBaseUser):
    matk = models.AutoField(db_column='MaTK', primary_key=True)
    hoten = models.CharField(db_column='HoTen', max_length=70)
    diachi = models.CharField(db_column='DiaChi', max_length=200, blank=True, null=True)
    sodienthoai = models.CharField(db_column='SoDienThoai', max_length=15, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
    isadmin = models.IntegerField(db_column='isAdmin', blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'taikhoan'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []   #email and password is required by default

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return str(self.isadmin)

    # @property
    # def is_active(self):
    #     return self.active

    @property
    def is_admin(self):
        return str(self.isadmin)

    objects = UserManager()
