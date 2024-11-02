from django.db import models

class Customer(models.Model):
    names = models.CharField('Nombres', max_length=60, blank=False, null=False)
    last_names = models.CharField('Apellidos', max_length=60, blank=False, null=False)
    cedula = models.CharField('Cédula', max_length=10, blank=False, null=False)
    address_home = models.CharField('Dirección Domiciliaria', max_length=100,blank=False,null=False)
    email = models.EmailField('Correo Electrónico', max_length=50, blank=False,null=False)
    phone = models.CharField('Número de Teléfono',max_length=10,blank=False,null=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.names} {self.last_names}'