import json
import csv

"""Читаем файл user.json"""
path_json = "users.json"
with open(path_json, "r") as read_file_json:
    data_json = json.load(read_file_json)

"""Читаем файл books.csv"""
path_csv = "books.csv"
results_csv = []
with open(path_csv, "r") as read_file_csv:
    data_csv = csv.DictReader(read_file_csv)
    for row in data_csv:
        """Получаем упорядочный словарь"""
        results_csv.append(row)
print(results_csv)

name_list = []
gender_list = []
address_list = []

"""Собираем списки данных"""
for id_dict in data_json:
    name = id_dict["name"]
    name_list.append(name)
    gender = id_dict["gender"]
    gender_list.append(gender)
    address = id_dict["address"]
    address_list.append(address)

user_dict = {}
too_json_list = []
"""Собираем словарь для передачи в json"""
for number in range(len(name_list)):
    too_json = {"name ": name_list[number], "gender: ": gender_list[number], "address ": address_list[number]}
    too_json_list.append(too_json)

"""Пишем в файл созданный словарь"""
with open("user_result", "w") as write_file_json:
    json.dump(too_json_list, write_file_json, indent=4)

"""
Записать файл json по структуре {
  "name": "Lolita Lynn",
  "gender": "female",
  "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
  "books": [
    {
      "title": "Fundamentals of Wavelets",
      "author": "Goswami, Jaideva",
      "height": "228"
      }
    
    ]
  
}"""

pass
