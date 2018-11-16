# CSV

import csv

with open('cars.csv') as f:
    cars = csv.DictReader(f)

    for car in cars:
        print(car['Brand'])
        print(car['Model'])
        print(car['Make'])
        print('\n')
