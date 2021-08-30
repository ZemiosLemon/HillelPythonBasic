import random


class House:
    def __init__(self, house_id):
        self.house_id = house_id
        self.settlers = random.randint(1, 100)


class Street:
    def __init__(self, street_id):
        self.list_houses = []
        self.street_id = street_id
        self.create_houses()

    def create_houses(self):
        for i in range(random.randint(5, 20)):
            self.list_houses.append(House(i))


class City:
    def __init__(self):
        self.list_streets = []
        self.create_streets(amount=7)

    def create_streets(self, amount):
        for num in range(amount):
            self.list_streets.append(Street(num))

    def delete_street(self, street_id):
        self.list_streets.pop(street_id)

    def add_street(self):
        self.list_streets.append(Street(len(self.list_streets)))

    def population(self):
        populations = 0
        for street in self.list_streets:
            for house in street.list_houses:
                populations += house.settlers
            return populations


    def table_city(self):
        with open('city_population.txt.txt', 'w') as file:
                file.write(f'{"Улица".rjust(10)}{"Дом".rjust(10)}Население\n')
                for street in self.list_street:
                    for house in street.list_houses:
                        file.write(f'{str(street.street_id).rjust(10)}{str(house.house_id).rjust(10)}{str(house.settlers)}\n')

gotham_city = City()
print(gotham_city.population())
gotham_city.table_city()
