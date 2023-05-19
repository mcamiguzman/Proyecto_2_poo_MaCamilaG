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
            print(f"{animal.name} added to {self.name}")
        else:
            print(f"Could not add {animal.name} to {self.name}")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} removed from {self.name}")
        else:
            print(f"{animal.name} not found in {self.name}")

    def show_animals(self):
        print(f"{self.name}:")
        for animal in self.animals:
            print(f"  {animal.name} ({animal.species}), {animal.age} years old, {animal.health_status}")