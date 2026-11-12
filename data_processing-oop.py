import csv, os


class CityData:
    def __init__(self, filename):
        location = os.path.dirname(os.path.realpath(__file__))
        self.cities = []
        with open(os.path.join(location, filename)) as f:
            rows = csv.DictReader(f)
            for row in rows:
                self.cities.append(dict(row))

    def first_five(self):
        for city in self.cities[:5]:
            print(city)

    def average_temperature(self):
        temps = [float(city['temperature']) for city in self.cities]
        return sum(temps) / len(temps)

    def cities_in_country(self, country):
        return [city['city'] for city in self.cities if city['country'] == country]

    def cities_above_temperature(self, country, temperature):
        return [city['city'] for city in self.cities
                if city['country'] == country and float(city['temperature']) > temperature]

    def unique_countries(self):
        return len(set(city['country'] for city in self.cities))

    def country_average_temperature(self, country):
        temps = [float(city['temperature']) for city in self.cities if city['country'] == country]
        return sum(temps) / len(temps)

    def country_max_temperature(self, country):
        temps = [float(city['temperature']) for city in self.cities if city['country'] == country]
        return max(temps)


data = CityData('Cities.csv')

# Print first 5 cities only
data.first_five()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(data.average_temperature())
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(data.average_temperature())
print()

# Print all cities in Germany
print("All cities in Germany:")
for city in data.cities_in_country('Germany'):
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
for city in data.cities_above_temperature('Spain', 12):
    print(city)
print()

# Count the number of unique countries
print(data.unique_countries())
print()

# Print the average temperature for all the cities in Germany
print(data.country_average_temperature('Germany'))
print()

# Print the max temperature for all the cities in Italy
print(data.country_max_temperature('Italy'))