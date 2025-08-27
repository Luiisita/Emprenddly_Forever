# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, DECIMAL, Float
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "usuarios"

    Id_Usuarios = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), unique=True, index=True, nullable=False)  
    Email = Column(String(100), unique=True, index=True, nullable=False)
    Telefono = Column(String(20))
    Contraseña = Column(String(255), nullable=False) 
    Rol = Column(String(50), nullable=False)          
    Estado = Column(String(20), default="activo")


class MetodoPago(Base):
    __tablename__ = "metodo_pago"

    Id_Metodo = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(50), nullable=False)
    Descripcion = Column(Text)


class Producto(Base):
    __tablename__ = "productos"

    Id_Productos = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), nullable=False)
    Precio = Column(Float, nullable=False)

    ventas = relationship("RegistroVentas", back_populates="producto")


class RegistroVentas(Base):
    __tablename__ = "registro_ventas"

    Id_Venta = Column(Integer, primary_key=True, index=True)
    Id_Productos = Column(Integer, ForeignKey("productos.Id_Productos"), nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Id_Metodo = Column(Integer, ForeignKey("metodo_pago.Id_Metodo"), nullable=False)
    Id_Usuarios = Column(Integer, ForeignKey("usuarios.Id_Usuarios"), nullable=False)
    Fecha = Column(Date, nullable=False)

    producto = relationship("Producto", back_populates="ventas")
    metodo_pago = relationship("MetodoPago")
    usuario = relationship("User")


class ReporteVentas(Base):
    __tablename__ = "reporte_ventas"

    Id_Reporte = Column(Integer, primary_key=True, index=True)
    Id_Usuarios = Column(Integer, ForeignKey("usuarios.Id_Usuarios"), nullable=False)
    Id_Productos = Column(Integer, ForeignKey("productos.Id_Productos"), nullable=False)
    Id_Venta = Column(Integer, ForeignKey("registro_ventas.Id_Venta"), nullable=False)
    Fecha = Column(Date, nullable=False)

    usuario = relationship("User")
    producto = relationship("Producto")
    venta = relationship("RegistroVentas")


class ReporteGanancias(Base):
    __tablename__ = "reporte_ganancias"

    Id_Reporte = Column(Integer, primary_key=True, index=True)
    Fecha = Column(Date, nullable=False)
    Id_Venta = Column(Integer, ForeignKey("registro_ventas.Id_Venta"), nullable=False)
    Monto = Column(DECIMAL(10, 2), nullable=False)
    Id_Metodo = Column(Integer, ForeignKey("metodo_pago.Id_Metodo"), nullable=False)
    Id_Productos = Column(Integer, ForeignKey("productos.Id_Productos"), nullable=False)

    venta = relationship("RegistroVentas")
    metodo_pago = relationship("MetodoPago")
    producto = relationship("Producto")


class ReporteDePedido(Base):
    __tablename__ = "reporte_pedidos"

    Id_REP = Column(Integer, primary_key=True, index=True)
    Fecha_Generacion = Column(Date, nullable=False)
    Estado = Column(String(50), nullable=False)
    Formato = Column(String(50), nullable=False)
    Id_Usuarios = Column(Integer, ForeignKey("usuarios.Id_Usuarios"), nullable=False)
    Id_Venta = Column(Integer, ForeignKey("registro_ventas.Id_Venta"), nullable=False)

    usuario = relationship("User")
    venta = relationship("RegistroVentas")


class RegistroGasto(Base):
    __tablename__ = "registro_gastos"

    Id_Gasto = Column(Integer, primary_key=True, index=True)
    Categoria = Column(String(50), nullable=False)
    Fecha = Column(Date, nullable=False)
    Monto = Column(DECIMAL(10, 2), nullable=False)
    Id_Venta = Column(Integer, ForeignKey("registro_ventas.Id_Venta"), nullable=False)

    venta = relationship("RegistroVentas")


class ReporteGasto(Base):
    __tablename__ = "reporte_gastos"

    Id_Repor_Gastos = Column(Integer, primary_key=True, index=True)
    Id_Gasto = Column(Integer, ForeignKey("registro_gastos.Id_Gasto"), nullable=False)
    Dia = Column(Date, nullable=False)
    Id_Metodo = Column(Integer, ForeignKey("metodo_pago.Id_Metodo"), nullable=False)

    gasto = relationship("RegistroGasto")
    metodo_pago = relationship("MetodoPago")


class RegistroInventario(Base):
    __tablename__ = "registro_inventario"

    Id_Inventario = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Valor_Unitario = Column(DECIMAL(10, 2), nullable=False)
    Id_Productos = Column(Integer, ForeignKey("productos.Id_Productos"), nullable=False)

    producto = relationship("Producto")


class ReporteInventario(Base):
    __tablename__ = "reporte_inventario"

    Id_ReportInventario = Column(Integer, primary_key=True, index=True)
    Id_Productos = Column(Integer, ForeignKey("productos.Id_Productos"), nullable=False)
    Fecha_Reporte = Column(Date, nullable=False)
    Cantidad_Producto = Column(Integer, nullable=False)
    Observaciones = Column(Text)

    producto = relationship("Producto")
