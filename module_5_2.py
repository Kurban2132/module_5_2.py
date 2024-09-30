class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(name, number_of_floors)


    def go_to(self, new_floor):
        self.new_floor = new_floor
        print(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")


    def __len__(self,):
        return self.number_of_floors


    def __str__(self):
        str = "Название: < название >, кол-во этажей: < этажи >"
        return str

    
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

