import csv
print ("Stand by please, building list......")
#r = raw_input("Enter Yes or No: ") # -- ASk if you want Yes people or No people
ylst = list() # Create empty list for Yes People
nlst = list() # Create empty list for No people
d = dict()  # Create a Dictionary if needed
with open('vcwater.csv', 'rb') as f:
    reader = csv.reader(f)
# the code below will sort the rows into two list ylst and nlst based on what they start with
    for row in f:
        row = row.rstrip()
        if row.startswith("Yes"):
            ylst.append(row[4:])
        if row.startswith("No"):
            nlst.append(row[3:])
#this is a test line       
print ylst
print nlst
