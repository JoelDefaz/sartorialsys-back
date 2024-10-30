from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)  # Cambiado a self._db
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=100)
    name = models.CharField('Nombres', max_length=255, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    historical = HistoricalRecords()

    # Definición de roles
    ADMIN = 'administrativo'
    MANAGER = 'gerente'
    COUNTER = 'contador'
    EMPLOYEE = 'empleado'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Gerente'),
        (COUNTER, 'Contador'),
        (EMPLOYEE, 'Empleado')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)
    
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    # Configuración de USERNAME_FIELD y REQUIRED_FIELDS
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role', 'name', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'

    # Métodos adicionales para roles
    def is_admin(self):
        return self.role == self.ADMIN
