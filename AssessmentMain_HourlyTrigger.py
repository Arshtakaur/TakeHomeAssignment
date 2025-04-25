import mysql.connector
import schedule

def function_task():
    import requests

    url = 'http://koresoftware-dev-ed.develop.my.salesforce.com/services/data/v63.0/queryAll/?q=SELECT+Id,IsDeleted,FirstName,LastName,DoNotCall+FROM+contact'
    token = "00DDn000002q7Dy!ARkAQPiS6vHowRgQ1pe7h15ST237OGHDmgznRr5QcNOXIxGXI4QL.RQ3A.jfDaMw.8yhYmb1H7M2W41OOQ4l05sf46oJNDWQ"
    header = {
        "access_token": "00DDn000002q7Dy!ARkAQPiS6vHowRgQ1pe7h15ST237OGHDmgznRr5QcNOXIxGXI4QL.RQ3A.jfDaMw.8yhYmb1H7M2W41OOQ4l05sf46oJNDWQ",
        "instance_url": "https://koresoftware-dev-ed.develop.my.salesforce.com",
        "id": "https://login.salesforce.com/id/00DDn000002q7DyMAI/005Dn000002M1PFIA0",
        "token_type": "Bearer",
        "issued_at": "1745532132964",
        "signature": "dORHYK5En5LeKCgEfzXN7zUIqZkjmxCYt2+NTZxiHzM=",
        "Authorization": "Bearer 00DDn000002q7Dy!ARkAQPiS6vHowRgQ1pe7h15ST237OGHDmgznRr5QcNOXIxGXI4QL.RQ3A.jfDaMw.8yhYmb1H7M2W41OOQ4l05sf46oJNDWQ"}

    response = requests.get(url, headers=header)
    print(response)

    responseData = response.json()
    records = responseData['records']
    return records


def my_task():
    donation_records= function_task()
    cnx = mysql.connector.connect(user='adventureworks_arshta', password='9jbtd4jnf95ZjWVf',
                                  host='kinterview-db.cluster-cnawrkmxrmmc.us-west-2.rds.amazonaws.com',
                                  database='adventureworks')
    cursor = cnx.cursor()
    query = """SELECT 
        EA.EmailAddress AS Email, 
        PP.Title, 
        PP.FirstName AS FirstName, 
        PP.MiddleName AS MiddleName, 
        PP.LastName as LastName,
        CONCAT(PP.FirstName, ' ', PP.MiddleName, ' ', PP.LastName) AS FullName,
        PP.Suffix AS Suffix, 
        PA.AddressLine1 AS Address1Street, 
        PA.AddressLine2 AS Address2Street ,
        PA.City AS Address1City, 
        PA.StateProvinceID AS Address2State, 
        PA.PostalCode AS Address1Zip, 
        PPP.PhoneNumber AS Phone1, 
        PPT.Name AS Phone1Type
    FROM Person_EmailAddress EA
    LEFT JOIN Person_Person PP ON EA.BusinessEntityID = PP.BusinessEntityID 
    LEFT JOIN Person_Address PA ON EA.EmailAddressID = PA.AddressID
    INNER JOIN Person_PersonPhone PPP ON EA.BusinessEntityID = PPP.BusinessEntityID
    INNER JOIN Person_PhoneNumberType PPT ON PPP.PhoneNumberTypeID = PPT.PhoneNumberTypeID
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    columns = cursor.column_names

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
    create_table_sql = f"CREATE TABLE IF NOT EXISTS CustomerLeads ({column_defs})"
    dest_cursor.execute(create_table_sql)

    delete_query = "DELETE FROM CustomerLeads"
    del_cursor = dest_cnx.cursor()
    del_cursor.execute(delete_query)

    insert_query = "INSERT INTO CustomerLeads VALUES ({})".format(", ".join(["%s"] * len(columns)))
    dest_cursor.executemany(insert_query, rows)
    dest_cnx.commit()
    dest_cursor.close()
    dest_cnx.close()

    print(f"Data for {len(rows)} rows transferred to the destination database.")
    print(f"Received {len(donation_records)} from Donation Datastore")

schedule.every().hour.do(my_task)

while True:
    schedule.run_pending()







