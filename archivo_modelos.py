# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class IndicadoresCompras(models.Model):
    id_indicador = models.AutoField(db_column='ID_Indicador', primary_key=True)  # Field name made lowercase.
    id_kpi = models.ForeignKey('Kpis', models.DO_NOTHING, db_column='ID_KPI', blank=True, null=True)  # Field name made lowercase.
    id_compra = models.ForeignKey('Compras', models.DO_NOTHING, db_column='ID_Compra', blank=True, null=True)  # Field name made lowercase.
    valor_medido = models.DecimalField(db_column='Valor_Medido', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_medicion = models.DateField(db_column='Fecha_Medicion')  # Field name made lowercase.
    cumplimiento = models.BooleanField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicadores_Compras'


class IndicadoresInventario(models.Model):
    id_indicador = models.AutoField(db_column='ID_Indicador', primary_key=True)  # Field name made lowercase.
    id_kpi = models.ForeignKey('Kpis', models.DO_NOTHING, db_column='ID_KPI', blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_Producto', blank=True, null=True)  # Field name made lowercase.
    valor_medido = models.DecimalField(db_column='Valor_Medido', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_medicion = models.DateField(db_column='Fecha_Medicion')  # Field name made lowercase.
    cumplimiento = models.BooleanField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicadores_Inventario'


class IndicadoresProveedores(models.Model):
    id_indicador = models.AutoField(db_column='ID_Indicador', primary_key=True)  # Field name made lowercase.
    id_kpi = models.ForeignKey('Kpis', models.DO_NOTHING, db_column='ID_KPI', blank=True, null=True)  # Field name made lowercase.
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='ID_Proveedor', blank=True, null=True)  # Field name made lowercase.
    valor_medido = models.DecimalField(db_column='Valor_Medido', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_medicion = models.DateField(db_column='Fecha_Medicion')  # Field name made lowercase.
    cumplimiento = models.BooleanField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicadores_Proveedores'


class IndicadoresVentas(models.Model):
    id_indicador = models.AutoField(db_column='ID_Indicador', primary_key=True)  # Field name made lowercase.
    id_kpi = models.ForeignKey('Kpis', models.DO_NOTHING, db_column='ID_KPI', blank=True, null=True)  # Field name made lowercase.
    id_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='ID_Orden', blank=True, null=True)  # Field name made lowercase.
    valor_medido = models.DecimalField(db_column='Valor_Medido', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_medicion = models.DateField(db_column='Fecha_Medicion')  # Field name made lowercase.
    cumplimiento = models.BooleanField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicadores_Ventas'


class Kpis(models.Model):
    id_kpi = models.AutoField(db_column='ID_KPI', primary_key=True)  # Field name made lowercase.
    nombre_kpi = models.CharField(db_column='Nombre_KPI', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    descripcion_kpi = models.CharField(db_column='Descripcion_KPI', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    valor_objetivo = models.DecimalField(db_column='Valor_Objetivo', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unidad_medida = models.CharField(db_column='Unidad_Medida', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha_creacion = models.DateField(db_column='Fecha_Creacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KPIs'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    apellido = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    ci = models.IntegerField()
    ruc = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=250, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Compras(models.Model):
    id_compra = models.AutoField(db_column='ID_compra', primary_key=True)  # Field name made lowercase.
    fecha_compra = models.DateField(db_column='Fecha_compra')  # Field name made lowercase.
    monto_total = models.DecimalField(db_column='Monto_total', max_digits=10, decimal_places=2)  # Field name made lowercase.
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='ID_proveedor', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='ID_estado', blank=True, null=True)  # Field name made lowercase.
    id_medio_pago = models.ForeignKey('MediosPago', models.DO_NOTHING, db_column='ID_medio_pago', blank=True, null=True)  # Field name made lowercase.
    fecha_creacion = models.DateField(db_column='Fecha_creacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compras'


class DetallesCompra(models.Model):
    id_detalle = models.AutoField(db_column='ID_detalle', primary_key=True)  # Field name made lowercase.
    id_compra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='ID_compra', blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_producto', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    precio_unitario = models.DecimalField(db_column='Precio_unitario', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalles_compra'


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    apellido = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    ci = models.IntegerField()
    rol = models.ForeignKey('Roles', models.DO_NOTHING)
    direccion = models.CharField(max_length=250, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'


class Estados(models.Model):
    id_estado = models.AutoField(db_column='ID_estado', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estados'


class MediosPago(models.Model):
    id_medio_pago = models.AutoField(db_column='ID_medio_pago', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medios_pago'


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    orden_detalle = models.ForeignKey('OrdenDetalle', models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING)
    empleado = models.ForeignKey(Empleados, models.DO_NOTHING)
    fecha_orden = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'


class OrdenDetalle(models.Model):
    id_orden_detalle = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Productos', models.DO_NOTHING)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_detalle'


class PagosCompras(models.Model):
    id_pago = models.AutoField(db_column='ID_pago', primary_key=True)  # Field name made lowercase.
    id_compra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='ID_compra', blank=True, null=True)  # Field name made lowercase.
    fecha_pago = models.DateField(db_column='Fecha_pago')  # Field name made lowercase.
    monto_pagado = models.DecimalField(db_column='Monto_pagado', max_digits=10, decimal_places=2)  # Field name made lowercase.
    id_medio_pago = models.ForeignKey(MediosPago, models.DO_NOTHING, db_column='ID_medio_pago', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagos_compras'


class Personas(models.Model):
    id_persona = models.AutoField(db_column='ID_persona', primary_key=True)  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='ID_estado', blank=True, null=True)  # Field name made lowercase.
    fecha_creacion = models.DateField(db_column='Fecha_creacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personas'


class Productos(models.Model):
    id_producto = models.AutoField(db_column='ID_producto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    precio_unitario = models.DecimalField(db_column='Precio_unitario', max_digits=10, decimal_places=2)  # Field name made lowercase.
    stock_actual = models.IntegerField(db_column='Stock_actual')  # Field name made lowercase.
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='ID_estado', blank=True, null=True)  # Field name made lowercase.
    fecha_alta = models.DateField(db_column='Fecha_alta', blank=True, null=True)  # Field name made lowercase.
    fecha_creacion = models.DateField(db_column='Fecha_creacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(db_column='ID_proveedor', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey(Personas, models.DO_NOTHING, db_column='ID_persona', blank=True, null=True)  # Field name made lowercase.
    nombre_empresa = models.CharField(db_column='Nombre_empresa', max_length=150, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='ID_estado', blank=True, null=True)  # Field name made lowercase.
    fecha_alta = models.DateField(db_column='Fecha_alta', blank=True, null=True)  # Field name made lowercase.
    fecha_creacion = models.DateField(db_column='Fecha_creacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedores'


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    detalles = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'roles'
