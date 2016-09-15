import csv

hi = open("occupations.csv", "rb")
reader = csv.reader(hi)
dic = {}
ctr = 0

for occupation in reader:
    print occupation
    
for occupation in reader:
    parsed = str(occupation).strip("[]")
    listy = parsed.split(",")
    dic[listy[0]] = listy[1]

print dic
    
