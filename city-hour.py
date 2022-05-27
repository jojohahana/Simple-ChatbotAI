import datetime  

while (True):
  city = input("Enter city: ")

  current_time = datetime.datetime.now()
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  
  if city == "Boston":
    hour = hour - 4 

  elif city == "Tokyo":
    hour = hour + 9

  elif city == "Chicago":
    hour = hour - 5 

  elif city == "Seattle":
    hour = hour - 7

  ## add more cities here
  elif city == "Cairo":
    hour = hour + 2
  
  elif city == "Shanghai":
    hour = hour + 8

  elif city == "Kolkata":
    hour = hour + 5
    minutes = minute + 30

  elif city == "Karachi":
    hour = hour + 5
    
  elif city == "exit": 
    break
    
  else:
    print(city, "is not added")
    city = "GMT" 

  print(city, str(hour) + ":" + str(minute) + ":" + str(second))