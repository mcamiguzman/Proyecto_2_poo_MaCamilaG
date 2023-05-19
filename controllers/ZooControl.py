import streamlit as st
import time


class ZooController:
    def __init__(self, modelo1, modelo2, vista):
        self.modelo1 = modelo1 #Habitat
        self.modelo2 = modelo2 #Animal
        self.vista = vista

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            try:
                animal = self.vista.menu_crear_animal()
                if animal:
                    self.modelo1.addcrear_producto(producto)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presentó un error creando el producto")
        if opcion == 2:
            try:
                animal = self.vista.menu_crear_animal()
                if animal:
                    self.modelo1.crear_producto(producto)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presentó un error creando el producto")
        if opcion == 3:
            self.vista.listar_productos(self.modelo.animales)
        if opcion == 4:
            self.vista.menu_actualizar_producto(self.modelo.productos)


    def aplicar_formato_tabla(self, productos):
        datos = []
        for producto in productos:
            datos.append([producto.id, producto.nombre, producto.descripcion, producto.precio])
        return datos