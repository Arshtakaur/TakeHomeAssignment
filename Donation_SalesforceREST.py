import requests
import pandas
import sqlalchemy
import json



def task1():
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

    records = responseData["records"]
    print(type(records))


task1()