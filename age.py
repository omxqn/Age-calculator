import datetime



def age_calculator(user_input):

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
          pass
          
          #-------------------------------------------
          # convert user inputs to days
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
  
  
  return f"Your age is : {int(total_days)} Years\nAnd {int(months)} Months\nAnd {int(days)} Days \nAnd {hours_now} Hours \n{12-int(months)} months, {30-int(days)} days, {24-hours_now } Hours left until your next birthday!!"

user = input("Birth date (DD MM YYYY or DD-MM-YY): ")
print(age_calculator(user))



