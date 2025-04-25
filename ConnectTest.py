import mysql.connector
cnx = mysql.connector.connect(user='adventureworks_arshta', password='9jbtd4jnf95ZjWVf',
                              host='kinterview-db.cluster-cnawrkmxrmmc.us-west-2.rds.amazonaws.com',
                              database='adventureworks')
cursor = cnx.cursor()
query = "SELECT * FROM Person_Person"
cursor.execute(query)
rows = cursor.fetchall()

columns = cursor.column_names

#for row in rows:
#    print(row)

cnx.close()

dest_cnx = mysql.connector.connect(
    user='dw_arshta',
    password='ZRegZh31Pr3R4Krn',
    host='kinterview-db.cluster-cnawrkmxrmmc.us-west-2.rds.amazonaws.com',
    port=3306,
    database='dw_arshta'
)
dest_cursor = dest_cnx.cursor()


column_defs = ', '.join([f"`{col}` TEXT" for col in columns])
create_table_sql = f"CREATE TABLE IF NOT EXISTS Person_Person_Copy ({column_defs})"
dest_cursor.execute(create_table_sql)


insert_query = "INSERT INTO Person_Person_Copy VALUES ({})".format(", ".join(["%s"] * len(columns)))
dest_cursor.executemany(insert_query, rows)
dest_cnx.commit()


dest_cursor.close()
dest_cnx.close()

print(f"Successfully transferred {len(rows)} rows to the destination database.")





