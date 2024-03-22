from asgiref.sync import sync_to_async
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    async def acreate_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email for user must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(make_password(str(password)))
        await sync_to_async(user.save)()
        return user

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email for user must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('tg_id') is None:
            extra_fields.setdefault('tg_id', 0)
        return self.create_user(email, password, **extra_fields)
