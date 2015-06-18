import pyodbc


con = pyodbc.connect("DSN=MSSQL-PYTHON")
cursor = con.cursor()
live = raw_input("Enter Live webcast ID: ")
#dateval = raw_input("Enter Date with /'s  (example 01/01/2015): ")
cursor.execute('Select evt_key from ev_event where evt_code = ?',live)
rows = cursor.fetchone()
for row in rows:
    row = row.split()
print row
#===============================================================================
# cursor.execute('Select top 10 * from co_customer')
# rows2 = cursor.fetchall()
#===============================================================================

#Part 2 getting the Session
cursor.execute ('Select ses_code from ev_session where ')


#===============================================================================
# cursor.execute(("SELECT  cst_key AS reg_cst_key, reg_evt_key = ") + "'" + rows[0] + "', " +  "reg_registration_date = '" + dateval + "'," + "cst_org_name_dn AS reg_org_name_dn ,cst_ixo_key AS reg_ixo_key ,cst_cxa_key AS reg_cxa_key ,cst_cph_key AS reg_cph_key ,cst_eml_key AS reg_eml_key , cst_cfx_key AS reg_cfx_key , reg_rgt_key = 'C916D3DB-0EE4-4EC4-8B65-622BD6D20258' , reg_attendance_flag = '1'  FROM    co_customer") #   WHERE   cst_recno IN ())
# test = cursor.fetchall()
# print test
#===============================================================================