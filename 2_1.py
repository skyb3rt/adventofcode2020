import csv

count = 0
with open ("2.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        password = row[2]
        letter = row[1].replace(":","")
        parts = row[0].split("-")
        low = int(parts[0])
        high = int(parts[1])
        antall = password.count(letter)
        if low <= antall and antall <= high:
            count +=1
            #print (password,letter,low,high,antall) 
print (count)