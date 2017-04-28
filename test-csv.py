# -*- coding: utf-8 -*-
import csv


csvfile=open('dati.csv', 'r')
reader = csv.DictReader(csvfile, delimiter=";")

for row in reader:
    print (row['nome'] + ' ' + row['cognome'])


