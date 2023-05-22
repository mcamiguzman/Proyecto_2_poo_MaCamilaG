import streamlit as st
class Habitat:
    def __init__(self, name, temperature, diet, max_capacity):
        self.name = name
        self.temperature = temperature
        self.diet = diet
        self.max_capacity = max_capacity
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        else:
            self.animales = []
            st.session_state["animales"] = []


    def add_animal(self, animal):
        if len(self.animals) < self.max_capacity and self.diet == animal.diet:
            self.animals.append(animal)

