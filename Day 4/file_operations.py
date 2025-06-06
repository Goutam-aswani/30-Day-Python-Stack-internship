import csv
import json
import os

base_path = "Z:/Python/day4/combined_output"
os.makedirs(base_path, exist_ok=True)

csv_data = [
    ["Name", "Age", "Gender"],
    ["Goutam", 21, "Male"],
    ["Krish", 21, "Male"],
    ["Divya", 22, "Female"]
]

csv_path = os.path.join(base_path, "csv_data.csv")
with open(csv_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)
print(f"CSV file created at: {csv_path}")

json_data = {
    "name": "Goutam",
    "Age": 21,
    "company": "Valere Labs",
    "Designation": "Intern"
}
json_path = os.path.join(base_path, "my_data.json")
with open(json_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)
print(f"JSON file created at: {json_path}")

interns = ["Goutam", "Divya", "Arpit", "Krish", "Vidhi"]
txt_path = os.path.join(base_path, "interns.txt")
with open(txt_path, "w") as txt_file:
    for intern in interns:
        txt_file.write(f"{intern}\n")
print(f"TXT file created at: {txt_path}")

print("\nReading CSV")
with open(csv_path, "r") as csv_file:
    csv_content = csv.reader(csv_file)
    for line in csv_content:
        print(line)

print("\nReading JSON")
with open(json_path, "r") as json_file:
    json_content = json.load(json_file)
    for i, j in json_content.items():
        print(f"{i}:{j}")

print("\nReading TXT")
with open(txt_path, "r") as txt_file:
    print(txt_file.read())
