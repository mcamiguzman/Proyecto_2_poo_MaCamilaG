import streamlit as st
import time


class ZooController:
    def __init__(self, modelo1, modelo2, vista):
        self.modelo1 = modelo1 #Habitat
        self.modelo2 = modelo2 #Animal
        self.vista = vista

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            print("Listo")
        if opcion == 2:
            try:
                habitad = self.vista.menu_crear_hanitad()
                if habitad:
                    self.modelo1.menu_crear_habitat(habitad)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presentó un error creando el producto")
        if opcion == 3:
            self.vista.listar(self.modelo2.animales)
        if opcion == 4:
            print("Listo")


    def aplicar_formato_tabla(self, animales):
        datos = []
        for animal in animales:
            datos.append([animal.id, animal.nombre, animal.descripcion, animal.precio])
        return datos