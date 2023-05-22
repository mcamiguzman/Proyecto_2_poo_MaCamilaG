import Models.AnimalModel as AnumalModel
import Models.HabitadModel as HabitadModel
import controllers.ZooControl as ZooConrol
import streamlit as st
import pandas as pd

class Zoo:
    def __init__(self):
        self.habitat = HabitadModel.Habitat()
        self.animal = AnumalModel.Animal()
        self.controlador = ZooConrol.TiendaController(self.habitat,self.animal, self)
        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []
        if "animales" in st.session_state:
             self.habitats = st.session_state["animales"]
        else:
            self.animales = []
            st.session_state["animales"] = []

    def mostrar_menu(self):
        st.title("Bienvenido al Zoo")

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Crear Habitad")
            boton_crear_producto = col1.button("Acceder a esta opción", 1)
            col2.header("Crear Animal")
            boton_listar_productos = col2.button("Acceder a esta opción", 2)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Listar Animales")
            boton_actualizar_producto = col1.button("Acceder a esta opción", 3)
            col2.header("Editar Comidas")
            boton_borrar_producto = col2.button("Acceder a esta opción", 4)

        if boton_crear_producto:
            st.session_state["opcion"] = 1
        elif boton_listar_productos:
            st.session_state["opcion"] = 2
        elif boton_actualizar_producto:
            st.session_state["opcion"] = 3
        elif boton_borrar_producto:
            st.session_state["opcion"] = 4

        if "opcion" in st.session_state:
            self.controlador.ejecutar_opcion(st.session_state["opcion"])

    def listar(self, animales):
        st.divider()
        with st.container():
            st.subheader("Listado de animales")
            if len(animales) == 0:
                st.error("No hay animales")
            else:
                datos = pd.DataFrame(
                    self.controlador.aplicar_formato_tabla(animales),
                    columns=["Nombre", "Edad", "Habiatat","Alimento"]
                )

                st.table(datos)

    def menu_crear_habitat(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo habitad")
            name = st.selectbox("Cual desea agregar",("desertico", "selvatico", "polar" , "acuatico"))
            temperature = st.number_input("Introduzca la temperatura")
            diet = st.selectbox("Seleccion una dieta", ("desertico", "selvatico", "polar", "acuatico"))
            max_capacity = st.number_input("Introduzca la temperatura")
            boton_accion = st.button("Crear nuevo habitat")

        if boton_accion:
            if not (-30 <= temperature <= 40) :
                raise ValueError("Temperatura incoherente")
            if not (0 <= max_capacity <= 30) :
                raise ValueError("Numero con aceptable")

            nuevoHabitat = HabitadModel.Habitat(name, temperature, diet, max_capacity)
            Zoo.habitats.append(nuevoHabitat)
            st.success("El Animal fue creado correctamente")
            return nuevoHabitat

    def menu_crear_animal(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo Animal")
            habitat = st.selectbox("Cual desea agregar", ("desertico", "selvatico", "polar", "acuatico"))
            health_status = st.text_input("Introduzca estado de salud")
            age = st.number_input("Introduzca la edad del animal")
            name = st.text_input("Introduzca el nombre del animal")
            diet = st.selectbox("Seleccion una dieta", ("desertico", "selvatico", "polar", "acuatico"))
            species = st.text_input("Introduzca especie del animal")
            boton_accion = st.button("Crear nuevo producto")

        if boton_accion:
            if habitat in Zoo.habitats:
                nuevoAnimal = AnumalModel.Animal(name, species, age, diet, health_status, habitat)
                it = Zoo.habitats[habitat]
                #Zoo.Habitats[it]=Todo

            st.success("El producto fue creado correctamente")
            return nuevoAnimal

    def cambio_alimento(self):
        # No se alcanzo a terminar la funcion
        # Pero lo que se queria a hacer es buscar identificar el animal por el nombre, pedir el alimeto a cambiar como
        # el cambio y llamar a funcion de la clase animal

        for animal in Zoo.animales:
            if animal.diet == "Carivoro":
                animal.alimento()


    def obtener_informacion(self, nombre, productos):
        for producto in productos:
            if producto.nombre == nombre:
                return producto

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)
