import json

data = []

with open('etmgeg_344.txt') as file:
    lines = file.readlines()

    for i in range(53, len(lines)):

        elements = lines[i].split(",")

        try:
            min_temp = int(elements[12]) / 10
            max_temp = int(elements[14]) / 10
            date = elements[1]

        except:
            continue;

        if min_temp > 18 or max_temp > 25:
            data.append({"date": date[:4] + " " + date[4:6] + " " + date[6:8], "min_temp": min_temp, "max_temp": max_temp})

count = 0
sum = 0
current_year = "1957"
year_data = {"1957": []}
for element in data:
    year = element['date'][:4]
    if year == current_year:
        year_data[year].append(element)
    else:
        #print(current_year, ": ", len(year_data[str(current_year)]))
        print(len(year_data[str(current_year)]))
        sum += len(year_data[str(current_year)])
        count += 1
        current_year = year
        year_data[current_year] = []

print(current_year, ": ", len(year_data[str(current_year)]))

print("Average: ", sum / count)

print(json.dumps(year_data, indent=4))
