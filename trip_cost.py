<<<<<<< HEAD
<<<<<<< HEAD
def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
 
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3 and days <7:
    cost -=20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))
=======
def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
 
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3 and days <7:
    cost -=20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))
>>>>>>> caa7a19daf82ef17cbd26673297aabeac62a1417
=======
def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
 
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3 and days <7:
    cost -=20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))
>>>>>>> a3c79e1e64543b0d6f078d5527564506ecdfc6db
