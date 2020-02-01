import csv
import json
import requests

with open("data-input.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        r = requests.post("http://103.43.47.40/pelayanan/web/api/penduduk/create", data=row)
        print(r.text)
