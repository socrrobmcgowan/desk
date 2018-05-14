import requests
import json
import csv

ips = []
ip_reader = csv.reader(open('/Users/robbiemcgowan/ip.csv', newline= ''))

for row in ip_reader : 
    ips.append(row[0])
    
print(ips)
