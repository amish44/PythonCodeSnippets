import csv
import random

records=50000
print(f"Creating {records} records")

columnnames=['first_names','last_names','address_cities','title','contact_number','company','email', 'stage','linkedin_url']
writer = csv.DictWriter(open("people.csv", "w"), fieldnames=columnnames)

first_names=['Fn']
last_names=['Ln']
address_cities=['city']
title=['title']
contact_number=[1011111110]
company=['apple','facebook','Meta','Alphabet','Microsoft','Amazon','Tesla','Apolloio','Zensar','Infosys','TCS']
email=['test@uniqueemail.com']
stage=['Cold','Approaching','Replied','Interested','Not Interested','Do Not Contact','Bad data','Changed Job','Unresponsive']
linkedin_url=['http://www.linkedin.com/in/test']

writer.writerow(dict(zip(columnnames, columnnames)))
for i in range(0, records):
    writer.writerow(dict([
        ('first_names', first_names[0]+str(i)),
        ('last_names', last_names[0]+str(i)),
        ('address_cities', address_cities[0]+str(i)),
        ('title', title[0]+str(i)),
        ('contact_number', int(contact_number[0])+i),
        ('email', email[0].replace('test', 'test'+str(i))),
        ('company', random.choice(company)),
        ('stage', random.choice(stage)),
        ('linkedin_url', linkedin_url[0].replace('test','test'+str(i)))]))
