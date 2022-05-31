import csv
import json

model = "Model"
year = "Year"
horsepower = "Horsepower"
engine_size = "Engine_sizer"
headline = [model,year,horsepower,engine_size]
sneakers = []

with open("PYTHON/lesson10/auto.csv", 'r') as f:
     reader = csv.DictReader(f,headline)
     isFirst = True
     for line in reader:
        if isFirst:
            isFirst = False
            continue
        sneakers.append(line)
#        print(f"{line[model]}: {line[year]} {line[horsepower]} {line[engine_size]}")


with open('PYTHON/lesson10/auto_new.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerows(sneakers)
#    print(f"{line[model]}: {line[year]} {line[horsepower]} {line[engine_size]}")

to_json = {"Model":model}, {"Year":year}, {"Horsepower":horsepower}, {"Engine_sizer":engine_size}
print(to_json)
with open('PYTHON/lesson10/auto_new.json', 'w') as to_json:
    writer.writerows(to_json)