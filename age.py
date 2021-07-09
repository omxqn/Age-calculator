import datetime

#Date
year_now = datetime.datetime.now().year
month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day
#Time
hours_now = datetime.datetime.now().hour
minuts_now = datetime.datetime.now().minute
sec_now = datetime.datetime.now().second
while True:
    try:
        user_input = input("Birth date (DD MM YYYY or DD-MM-YY): ")
        try:
            age_year = (int(user_input.split(" ")[2]) * 12) * 30
            age_month = (int(user_input.split(" ")[1])) * 30
            age_day = int(user_input.split(" ")[0])
        except:
            age_year = (int(user_input.split("-")[2]) * 12) * 30
            age_month = (int(user_input.split("-")[1])) * 30
            age_day = int(user_input.split("-")[0])
            
        break
    except Exception as es:
        print("Please enter only numbers ")
#-------------------------------------------
# convert user inputs to days

#-------------------------------------------
# convert current date to days
year_now *= 30 * 12
month_now *= 30
#-------------------------------------------
# summ all days
sum_days = age_year + age_month + age_day
now_sum_days = year_now + day_now + month_now
#-------------------------------------------
# Get the subtraction of the days
total_days = now_sum_days - sum_days
#-------------------------------------------

total_days = total_days / 360 # Convert day -> year
months = (total_days-int(total_days)) * 12 # Convert day -> months  (in intiger)

days = (months - int(months)) * 30 # Get the subtraction of months and convert it to # Convert months -> days


print(f"Your age is : {int(total_days)} Years\nAnd {int(months)} Months\nAnd {int(days)} Days")
