import csv

count = 0
with open ("2.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        password = row[2].strip()
        letter = row[1].replace(":","")
        parts = row[0].split("-")
        first = int(parts[0])
        secound = int(parts[1])
        if password[first-1] != password[secound-1]:
            if letter == password[first-1] or letter == password[secound-1]:
                #print(letter,password[first-1],password[secound-1])
                count+=1
print (count)