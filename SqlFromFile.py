import pyodbc
import csv
import numpy as np

#-------------------------------------------------------------------------
#  Get the list of CSV users into variables for the first SQL Statement
#-------------------------------------------------------------------------
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


#===============================================================================
# This section will connect to SQL and put the GUID into a 
#===============================================================================
con = pyodbc.connect("DSN=MSSQL-PYTHON")
cursor = con.cursor()
#===============================================================================
# live = raw_input("Enter Live webcast ID: ")
#===============================================================================
live = '698-4-14wc'
#===============================================================================
# evtdate = raw_input ("Enter the Date of the webcast: ")
#===============================================================================
evtdate = '12/12/12'
sql_command = ("""Select evt_key from ev_event where evt_code = ?""")
cursor.execute(sql_command,live)
evtguid = cursor.fetchone()
for evt in evtguid:
    evt = evt.split()
#print evt

#============================================================================
# Get the Session Key
#============================================================================
sql_command = ("Select ses_key from ev_session where ses_evt_key = ?")
cursor.execute(sql_command, evt)
session = cursor.fetchone()
#print session


sql_command = ("""
               select cst_key as reg_cst_key, 
               --reg_evt_key = ?, 
               --reg_registration_date =?,
               cst_org_name_dn as reg_org_name_dn,
               cst_ixo_key as reg_ixo_key, 
               cst_cxa_key as reg_cxa_key,
               cst_cph_key as reg_cph_key,
               cst_eml_key as reg_eml_key, 
               cst_cfx_key as reg_cfx_key,
               reg_rgt_key = 'C916D3DB-0EE4-4EC4-8B65-622BD6D20258' ,
               reg_attendance_flag = '1'
               FROM    co_customer
               WHERE   cst_recno IN (                 
               """)

for item in ylst:
    sql_command += "'" + item + "',"

sql_command = sql_command[:-1]
sql_command += ")"
               
#print(sql_command)
cursor.execute(sql_command)
results = cursor.fetchall()
for result in results:
    print result



#===============================================================================
# 
# def List2SQLList(items):
#     sqllist = "%s" % "\",\"".join(items)
#     return sqllist
# #print List2SQLList(ylst)
# 
# ##  Try to convert ylist to an array
# ylist = np.asarray(ylst)
# print ylist
# 
# 
# print evtdate
# 
# sql_command = ("""
#                select cst_key as reg_cst_key, 
#                reg_evt_key = ?, 
#                reg_registration_date =?,
#                cst_org_name_dn as reg_org_name_dn,
#                cst_ixo_key as reg_ixo_key, 
#                cst_cxa_key as reg_cxa_key,
#                cst_cph_key as reg_cph_key,
#                cst_eml_key as reg_eml_key, 
#                cst_cfx_key as reg_cfx_key,
#                reg_rgt_key = 'C916D3DB-0EE4-4EC4-8B65-622BD6D20258' ,
#                reg_attendance_flag = '1'
#                FROM    co_customer
#                WHERE   cst_recno IN ( + ','.
#                  
#                """)
# cursor.execute(sql_command, evt(0), evtdate, ["ylist"])
# allpeople = cursor.fetchall()
# print allpeople
# 
# #  URL for reference to try Hopefully it will work.
# 
# #===============================================================================
# # http://stackoverflow.com/questions/4819356/sql-in-operator-using-pyodbc-and-sql-server
#===============================================================================
