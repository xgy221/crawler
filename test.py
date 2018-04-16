import requests
import csv

with open("test.csv", "w", newline="") as w:
    writer = csv.writer(w)
    writer.writerow('\xae')


