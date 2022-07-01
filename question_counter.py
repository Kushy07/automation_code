import csv

with open('testseries_student_reportcards (5).csv','r') as csv_file:
    counts = dict()
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        words = line['incorrect'].split(',')
        for word in words:
            counts[word] = counts.get(word,0) + 1

temp = list()
for k, v in counts.items():
    temp.append( (v,k) )



temp = sorted(temp, reverse = True)
# print(temp)


with open('qid_frequency.csv','w',newline='') as w_csv:
    csv_out = csv.writer(w_csv)
    csv_out.writerow(['qid','frequency'])
    for row in temp:
        csv_out.writerow(row)
