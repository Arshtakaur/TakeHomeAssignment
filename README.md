# TakeHomeAssignment

The code shall be executed from the AssessmentMain_HourlyTrigger.py file

To run the main file. Please modify the following:-
-> Update the value at issued_at - on line 14
-> Update the signature - on line 15
-> Update the access_token value - on line 10
-> Update the value of the token on field Authorization - on line 16


These values can be obtained by making a POST call to the following URL - https://login.salesforce.com/services/oauth2/token

The request body for the call is the following:

```
grant_type: password
client_id: Your_client_ID
client_secret: Your_client_secret
username: Your_username
password: Your_password
```
Please ensure the request body is of type ```x-www-form-urlencoded```.
