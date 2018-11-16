# FINAL

# Car Model { 'Brand': 'Honda', 'Model': 'Accord EX', 'Make': '2012' }

import csv
import unittest


class CarFinder:
    cars = []

    def __init__(self, *args, **kwargs):
        with open('cars.csv') as f:
            self.cars = list(csv.DictReader(f))

    def find_car_by_year(self, year):
        for car in self.cars:
            if car['Make'] == year:
                return car


class PrimesTestCase(unittest.TestCase):
    def test_car_finder(self):
        car_finder = CarFinder()
        min_car = car_finder.find_car_by_year()
        self.assertTrue(type(min_car['Brand']))
        self.assertTrue(type(min_car['Model']))
        self.assertTrue(min_car['Make'].isdigit())


def main():
    car_finder = CarFinder()
    min_car = car_finder.find_car_by_year("2014")
    print("brand: ", min_car['Brand'])
    print("model: ", min_car['Model'])
    print("make: ", min_car['Make'])


if __name__ == '__main__':
    main()
    # unittest.main()