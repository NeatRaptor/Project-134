import pandas as pd
import csv
import matplotlib as plt

rows = []

with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(len(star_data_rows))

distance_suitable_stars = []
for star_data in star_data_rows:
    if float(star_data[2]) <= 100:
        distance_suitable_stars.append(star_data)
print(len(distance_suitable_stars))

suitable_stars = []
for star_data in distance_suitable_stars:
    if float(star_data[5]) > 150 and float(star_data[5]) < 350:
        suitable_stars.append(star_data)
print(len(suitable_stars))

with open("final.csv","a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(suitable_stars)