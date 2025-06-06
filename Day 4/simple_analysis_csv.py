filename = "Z:/Python/data.csv"
data = open(filename, 'r')
lines = data.readlines()

data.close()

for line in lines:
    print(line.strip())


data1 = []
for line in lines:
    values = line.strip().split(',')
    data1.append(values)

for row in data1:
    print(row)

headers = data1[0]
rows = data1[1:]

print("Headers:", headers)
print("Data:", rows)

f_count = 0
for row in rows:
    if row[2].lower() == 'female':
        f_count += 1
print(f"Number of females: {f_count}")

total_age = 0
count = 0
for row in rows:
    total_age += int(row[1])
    count += 1

average_age = total_age / count
print(f"Average age: {average_age}")
