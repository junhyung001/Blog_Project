from typing import Any
from django.db import models

# Create your models here.

from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, AbstractUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password, staff=False, admin=False, active=True):
        if not email:
            raise ValueError("이메일을 입력해주새요!")
        if not password:
            raise ValueError('비밀번호를 입력해주세요!')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.staff = staff
        user.admin = admin
        user.active = active
        user.save(using=self._db)
        
    def create_superuser(self, email, password):
        user = self.create_user(
                email,
                password,
                staff = True,
                admin=True
        )
        
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
        
    
    def __str__(self):
        return self.email
    
    def is_staff(self):
        return self.staff

    def is_superuser(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        return self.admin
    
    def has_module_perms(self, app_label):
        return self.admin

    
# class BaseUserManager(models.Manager):
#     def normalize_email(cls, email):
#         """
#         Normalize the email address by lowercasing the domain part of it.
#         """
#         email = email or ''
#         try:
#             email_name, domain_part = email.strip().rsplit('@', 1)
#         except ValueError:
#             pass
#         else:        
#             email = email_name + '@' + domain_part.lower()
#         return email