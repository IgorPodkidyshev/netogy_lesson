import csv

with open('https://replit.com/@IghorPodkidyshi/netologyfileformats221006#files/newsafr.csv') as fileCSV:
    readerCSV = csv.reader(fileCSV)
    for line in readerCSV:
        print(line[-1])