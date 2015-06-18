import _mssql
conn = _mssql.connect(server = '10.50.1.237', user = 'stephenc', password = 'trust.me1', database = 'nfgcsaadevms')
conn.execute_query("Select top 1 * from co_address_ext")
res1 = [ row for row in conn ]
print res1