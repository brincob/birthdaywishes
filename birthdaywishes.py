import datetime
import time
import requests
import json
#import pandas
import random
import smtplib

year = int(datetime.datetime.now().strftime("%Y"))
#year = 2024
# To get year (integer input) from the user
# year = int(input("Enter a year: "))

def leap_func(year):
    
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return("{0} is a leap year".format(year))
    
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        return("{0} is a leap year".format(year))
    
    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return("{0} is not a leap year".format(year))   
    
#print(leap_func(year))

# Get data from realm digital api
def get_api_data():

	r = requests.get("https://interview-assessment-1.realmdigital.co.za/do-not-send-birthday-wishes")

	return r.json()

api_data = get_api_data()


my_email = "your_email@gmail.com"
passw = "your_password"

#data = pandas.read_csv("birthdays.csv")

today = datetime.datetime.now()
bday = api_data[(api_data.month == today.month) & (api_data.day == today.day)]
name = bday["name"].tolist()
email = bday["email"].tolist()
status = bday["status"].tolist()

employees = []

for n in range(len(name)):
    employees.append(
        {
            "name": name[n],
            "email": email[n]
            "status": status[n]
        }
    )

if not in employees:
    print("no birthdays today")
    # stops the current iteration and continues with the next one
    continue
elif  employees["status"] == "No Longer Employee":
    print("Employee no longer works for Realm Digital")
    continue
elif  employees["status"] == "Not Yet Employee":
    print("Is not yet a Realm Digital Employee")
    continue 
elif  employees["status"] == "No Birthday Wishes":
    print("Is not supposed to receive birthday wishes")
    continue    
else:
    for employee in employees:
        num = random.randint(1, 3)
        with open(f"letterTemplates/letter_{num}.txt") as letter:
            lines = letter.readlines()
            lines[0].strip()
            lines[0] = lines[0].replace("[NAME]", employee["name"])
            message = "".join(lines)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passw)
            connection.sendmail(from_addr=my_email, to_addrs=employee["email"], msg=f"Subject: HAPPY BIRTHDAY\n\n{message}")
            print(f"message sent to {employee['name']}" + leap_func(year))
            
            
                       
            