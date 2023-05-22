class Animal:
    def __init__(self, name, species, age, diet, health_status, habitat):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.health_status = health_status
        self.habitat = habitat


    def alimento(self,listAlimento,alimentoCambio,alimetoDip):
        if alimetoDip in listAlimento:
            index = listAlimento.index(alimetoDip)
            listAlimento[index] = alimentoCambio
            return "Cambio exitoso"
        else:
            return "Hay probelmas"



